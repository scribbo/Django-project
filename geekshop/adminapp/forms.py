from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authapp.models import ShopUser
from mainapp.models import Products, Category
from django.forms.widgets import HiddenInput
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

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = HiddenInput()
        
        
