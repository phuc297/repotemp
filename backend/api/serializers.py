from rest_framework import serializers

from posts.models import Post
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='user-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'content', 'author']


class UserSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='post-detail'
    )

    class Meta:
        model = User
        fields = ['username', 'author']
        # fields = ['username']
