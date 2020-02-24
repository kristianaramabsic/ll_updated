from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save

class CustomUser (AbstractUser):
    university = models.CharField (max_length=80)
    department = models.CharField (max_length=80, blank=True)
    country = CountryField(blank=True, blank_label='(enter country)')
    photo = models.ImageField(upload_to='images', blank=True, default='default/testimonial2.jpg')
    research_description = models.TextField (default="Tell others what is your research about...")

    def __str__(self):
        return self.username

    def get_absolute_url (self):
        return reverse ('user_profile:user_profile', args=[str(self.username)])

def create_profile (sender, **kwargs):
    if kwargs['created']:
        user_profile = CustomUser.objects.create(username=kwargs['instance'])

post_save.connect(create_profile, sender=AbstractUser)