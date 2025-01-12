from django.contrib import admin
from .models import Comment

admin.sites.register(Comment)
