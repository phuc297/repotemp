import random

from django.contrib.auth.models import User
from django.db import models

default_avatars = [
    "001-boy.png",
    "002-girl.png",
    "003-boy-1.png",
    "004-boy-2.png",
    "005-boy-3.png",
    "006-girl-1.png",
    "007-boy-4.png",
    "008-girl-2.png",
    "009-girl-3.png",
    "010-boy-5.png",
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name='following', blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def set_default_avatar(self):
        self.avatar = f"{random.choice(default_avatars)}"

    def __str__(self):
        return self.user.username
