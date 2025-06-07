from django.contrib import admin

from .models import Snippet, Vote

# Register your models here.

admin.site.register(Snippet)
admin.site.register(Vote)