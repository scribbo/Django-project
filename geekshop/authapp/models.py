import uuid
from datetime import timedelta
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


def get_activation_key_expires():
    return now() + timedelta(hours=24)


class ShopUser(AbstractUser): 
    city = models.CharField(max_length=64, blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True) 
    age = models.PositiveIntegerField(default=20)
    is_active = models.BooleanField(default=False)
    

    activation_key = models.UUIDField(default=uuid.uuid4)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    @property
    def is_activation_key_expires(self):
        return now() > self.activation_key_expires
    
    def activate(self):
        self.is_active = True
        self.activation_key_expires = now()
 