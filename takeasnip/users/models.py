from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Administrator')], default='user')
    xp = models.IntegerField(default=0)
    rank = models.CharField(max_length=20, choices=[
        ('begginer', 'Begginer Coder'), ('advanced', 'Advanced Coder'), ('master', 'Master Coder')
    ], default='begginer')