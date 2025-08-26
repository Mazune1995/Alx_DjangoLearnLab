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
# posts/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Prevent multiple likes
    like, created = Like.objects.get_or_create(user=user, post=post)

    if created:
        # ✅ Only notify if this is a new like
        if post.author != user:  # Don’t notify yourself
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )
        return JsonResponse({"status": "liked"})
    else:
        return JsonResponse({"status": "already liked"})


@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    like = Like.objects.filter(user=user, post=post).first()
    if like:
        like.delete()
        return JsonResponse({"status": "unliked"})
    else:
        return JsonResponse({"status": "not liked"})

