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

    def __str__(self):
        return self.title

    def get_votes(self, value):
        return Vote.objects.filter(snippet=self, value=value).count()

class Vote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'snippet')

class Comment(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

