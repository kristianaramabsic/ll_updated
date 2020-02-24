from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.db import models
from django.urls import reverse

class CustomUser (AbstractUser):
    university = models.CharField (max_length=80)
    department = models.CharField (max_length=80, blank=True)
    country = CountryField(blank=True, blank_label='(enter country)')
    photo = models.ImageField(upload_to='images', blank=True, default='default/testimonial2.jpg')
    research_description = models.TextField (default="Tell others what is your research about...")

    def get_absolute_url (self):
        return reverse ('user_profile', args=[str(self.username)])

