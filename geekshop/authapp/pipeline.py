""" from urllib import response
import requests

def get_user_gender(user, response, *args, **kwargs):
    access_token = response['access_token']
    vk_response = requests.get(
        f'https://api.vk.com/method/users.get?access_token={access_token}&fields=bdate,sex&v=5.131')
    user.profile.about = vk_response.text
    user.profile.save()
    return {} """

from collections import OrderedDict 
from datetime import datetime 
from urllib.parse import urlencode, urlunparse 
import requests 
from django.utils import timezone 
from social_core.exceptions import AuthForbidden 
from authapp.models import ShopUserProfile 

def get_user_gender(backend, user, response, *args,**kwargs): 
    if backend.name !='vk-oauth2': 
        return 
    api_url = urlunparse(('https', 'api.vk.com', '/method/users.get', None, 
            urlencode(OrderedDict(fields=','.join(('bdate','sex', 'about')), 
            access_token=response['access_token'], v='5.92')), 
        None
    )) 
    resp = requests.get(api_url) 
    if resp.status_code !=200: 
        return 
    
    data = resp.json()['response'][0] 
    if data['sex']: 
        user.profile.gender = ShopUserProfile.MALE if data['sex'] ==2 else ShopUserProfile.FEMALE 
    
    if data['about']: 
        user.profile.about = data['about'] 
    
    if data['bdate']: 
        bdate = datetime.strptime(data['bdate'],'%d.%m.%Y').date() 
        age = timezone.now().date().year - bdate.year 
    
    if age <18: 
        user.delete() 
        raise AuthForbidden('social_core.backends.vk.VKOAuth2') 
    user.save()