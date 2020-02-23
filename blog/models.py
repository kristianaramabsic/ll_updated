from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Post (models.Model):
    title = models.CharField (max_length=400)
    author = models.ForeignKey (get_user_model(), on_delete=models.CASCADE,)
    date = models.DateField (auto_now_add=True)
    text = models.TextField ()

    def __str__ (self):
        return self.title [:200]

    def get_absolute_url (self):
        return reverse ('post_detail', args=[str(self.id)])

