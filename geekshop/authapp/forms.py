from dataclasses import fields
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import ShopUser

class LoginForm(AuthenticationForm): 
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',)

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'age', 'avatar')

    def clean_city(self):
        data = self.cleaned_data["age"]
        if data <= 0:
            raise ValidationError ("Мы работаем в Санкт-Петербурге")
        return data
                    