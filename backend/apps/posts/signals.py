from django.db.models.signals import post_delete, post_save
from django.db.models import Sum
from django.dispatch import receiver
from .models import PostVote, Post

@receiver(post_delete, sender=PostVote)
@receiver(post_save, sender=PostVote)
def update_post_votes(sender, instance, **kwargs):
    post = instance.post
    total_value = post.post_votes.aggregate(total=Sum('value'))['total'] or 0
    post.votes = total_value
    post.save(update_fields=['votes'])