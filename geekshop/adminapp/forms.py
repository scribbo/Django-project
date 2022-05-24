from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authapp.models import ShopUser
from mainapp.models import Category
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',)
       
class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'age', 'avatar')

class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


        
