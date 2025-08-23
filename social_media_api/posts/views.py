from rest_framework import generics, permissions
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
        # Get the users that the current user follows
        following_users = self.request.user.following.all()
        # Filter posts by those users, ordered by newest first
        return Post.objects.filter(author__in=following_users).order_by("-created_at")

