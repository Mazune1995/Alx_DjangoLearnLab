from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

from .models import Post
from .serializers import PostSerializer


class FeedView(generics.ListAPIView):
    """
    Returns a feed of posts from users that the authenticated user follows.
    Ordered by most recent first.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users that the current user follows
        followed_users = self.request.user.following.all()
        # Return posts only from followed users, newest first
        return Post.objects.filter(author__in=followed_users).order_by("-created_at")

