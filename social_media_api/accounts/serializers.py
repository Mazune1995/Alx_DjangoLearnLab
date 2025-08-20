# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser, UserFollow

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source="followers.count", read_only=True)
    following_count = serializers.IntegerField(source="following.count", read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "followers_count", "following_count"]


class UserFollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source="follower.username")
    following = serializers.ReadOnlyField(source="following.username")

    class Meta:
        model = UserFollow
        fields = ["id", "follower", "following", "created_at"]

