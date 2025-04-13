from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification
from posts.models import Like, Comment
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.user,
            verb="liked your post",
            target=instance.post
        )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.author,
            verb="commented on your post",
            target=instance.post
        )