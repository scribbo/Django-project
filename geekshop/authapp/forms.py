from dataclasses import fields
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import ShopUser, ShopUserProfile

class LoginForm(AuthenticationForm): 
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email')
    
    def save(self, commit=True):
        user = super().save(commit)
        user.is_active = False
        user.save()
        return user

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'age', 'avatar')

    def clean_age(self):
        data = self.cleaned_data['age']
        if data <= 18:
            raise ValidationError ("Пользователь должен быть совершеннолетним")
        return data

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = ShopUserProfile
        fields = ('gender', 'about')
                