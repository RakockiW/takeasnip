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

    def get_upvotes(self):
        return VoteSnippet.objects.filter(snippet=self, value=1).count()

    def get_downvotes(self):
        return VoteSnippet.objects.filter(snippet=self, value=-1).count()

    def get_total_votes(self):
        return VoteSnippet.objects.filter(snippet=self).count()

    def get_total_comments(self):
        return Comment.objects.filter(snippet=self).count()

class Comment(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.content

    def get_upvotes(self):
        return VoteComment.objects.filter(comment=self, value=1).count()

    def get_downvotes(self):
        return VoteComment.objects.filter(comment=self, value=-1).count()

class VoteSnippet(models.Model):
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

class VoteComment(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'comment')



