from rest_framework import generics
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification

def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
        return JsonResponse({"status": "liked"})
    else:
        return JsonResponse({"status": "already liked"})


def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post).first()
    if like:
        like.delete()
        return JsonResponse({"status": "unliked"})
    else:
        return JsonResponse({"status": "not liked"})

