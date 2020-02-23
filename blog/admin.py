from django.contrib import admin
from .models import Post
from  threadedcomments.admin import ThreadedCommentsAdmin


admin.site.register (Post)