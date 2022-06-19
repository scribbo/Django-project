import uuid
from datetime import timedelta
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver


def get_activation_key_expires():
    return now() + timedelta(hours=24)


class ShopUser(AbstractUser): 
    city = models.CharField(max_length=64, blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True) 
    age = models.PositiveIntegerField(default=20)
    
    activation_key = models.UUIDField(default=uuid.uuid4)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    @property
    def is_activation_key_expires(self):
        return now() > self.activation_key_expires
    
    def activate(self):
        self.is_active = True
        self.activation_key_expires = now()
 
class ShopUserProfile(models.Model): 
    MALE= 'M' 
    FEMALE= 'F' 
    
    GENDER_CHOICES= ( 
        (MALE, 'Мale'), 
        (FEMALE, 'Female'), 
        ) 
    
    user = models.OneToOneField(ShopUser, related_name='profile', on_delete=models.CASCADE) 
    about = models.TextField(blank=True) 
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, blank=True)

@receiver(post_save, sender=ShopUser)
def  update_user_profile(sender, instance, created, **kwargs): 
    if created: 
        profile=ShopUserProfile(user=instance)
    else:
        profile=ShopUserProfile.objects.get(user=instance)
    profile.save()
    