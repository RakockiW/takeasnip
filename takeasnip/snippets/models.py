from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255)
    technology = models.CharField(max_length=255)

class Vote(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)


