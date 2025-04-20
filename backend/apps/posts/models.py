from django.conf import settings
from django_quill.fields import QuillField
import random

from django.contrib.auth.models import User
from django.db import models
from django.core.files import File

from django.utils.text import slugify

from apps.users.models import Profile
from utils.utils import get_random_thumbnail

colors = [
    "red",
    "yellow",
    "green",
    "blue",
    "pink",
    "purple"
]


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    color = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        available_colors = set(
            colors) - set(Category.objects.values_list("color", flat=True))
        if available_colors:
            self.color = random.choice(list(available_colors))
        else:
            raise ValueError("No available colors left to assign.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        Profile, related_name='posts', on_delete=models.CASCADE)
    title = models.TextField(blank=True, max_length=130)
    content = QuillField(blank=True)
    # content = models.TextField(blank=True)
    content_text = QuillField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, max_length=200)
    views = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='thumnail_post', null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_user_vote(self, profile_id):
        profile = Profile.objects.get(pk=profile_id)
        vote = self.post_votes.filter(voted_by=profile).first()
        return vote.value if vote else None


class PostVote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    )

    post = models.ForeignKey(Post, related_name='post_votes',
                             on_delete=models.CASCADE)
    voted_by = models.ForeignKey(
        Profile, related_name='votes', on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=VOTE_CHOICES)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voted_by', 'post')

    def __str__(self):
        return f"{self.voted_by} voted {self.get_value_display()} on {self.post}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    commenter = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    parent = models.ManyToManyField("self", symmetrical=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
