from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from snippets.models import Snippet, Comment, VoteSnippet, VoteComment
from .gamification import reward_user


@receiver(post_save, sender=Snippet)
def reward_for_snippet(sender, instance, created, **kwargs):
    if created:
        reward_user(instance.author, 'create_snippet')

@receiver(post_save, sender=Comment)
def reward_for_comment(sender, instance, created, **kwargs):
    if created:
        reward_user(instance.author, 'comment_snippet')

@receiver(post_save, sender=VoteSnippet)
@receiver(post_save, sender=VoteComment)
def reward_for_vote(sender, instance, created, **kwargs):
    if created:
        reward_user(instance.user, 'vote')