from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser): 
    city = models.CharField(max_length=64, blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True) 
    age = models.PositiveIntegerField(default=20)
    is_active = models.BooleanField(default=True)
