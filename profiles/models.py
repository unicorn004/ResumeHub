from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.

class Profile(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    contact_number = models.CharField(verbose_name='contact_number', max_length=10, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=100, blank=True)
    birth_date = models.TimeField(null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)  # LinkedIn URL
    instagram_url = models.URLField(max_length=200, blank=True)  # Instagram URL
    facebook_url = models.URLField(max_length=200, blank=True) # Facebook URL

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()