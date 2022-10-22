from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import Profile
from django.db.models.signals import pre_save
import os

@receiver(post_save, sender=User)
def create_profile(sender,instance, created,  **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance,  **kwargs):
    instance.profile.save()




@receiver(pre_save, sender=Profile)
def delete_old_file(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered 
    if instance._state.adding and not instance.pk:
        return False
    
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    
    # comparing the new file with the old one
    file = instance.image
    if not old_file == file:
        if os.path.isfile(old_file.path):
            print('deleted')
            os.remove(old_file.path)

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print('user logged out')