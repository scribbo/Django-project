from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from authapp.models import ShopUser
from authapp.forms import LoginForm, RegisterForm, UserEditForm
from .utils import send_verification_mail


def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user and user.is_active:
                auth.login(request,user=user)
                redirect_url = request.GET.get('next', reverse('index'))
                return HttpResponseRedirect(redirect_url)  
    return render(request, 'authapp/login.html', context={
        'title': 'Вход в систему',
        'form': form
        })


def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_mail(user)
            return HttpResponseRedirect(reverse('auth:login'))
    return render(request, 'authapp/register.html', context={
        'title': 'Регистрация',
        'form': form
        })


@login_required
def edit(request):
    form = UserEditForm(instance=request.user)
    
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'authapp/edit.html', context={
        'title': 'Редактирование профиля',
        'form': form
        })


def verify(request, email, key):
    try:
        user = ShopUser.objects.get(email=email, activation_key=key)
        if user.is_activation_key_expires:
            return render(request, 'authapp/verification.html', context={
                'message': 'Key is expired'
            })
        user.activate()
        user.save()
        return render(request, 'authapp/verification.html', context={
                'message': 'Success'
            })
    except ShopUser.DoesNotExist:
       return render(request, 'authapp/verification.html', context={
                'message': 'Verification failed'
            })
    

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
