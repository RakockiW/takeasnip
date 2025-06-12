from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField()
    category = models.CharField(max_length=255)
    technology = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Vote(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)

class Comment(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

