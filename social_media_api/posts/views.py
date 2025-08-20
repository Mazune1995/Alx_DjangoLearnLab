# posts/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post            
from accounts.models import CustomUser, UserFollow  
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get the IDs of users this user is following
        following_users = UserFollow.objects.filter(follower=user).values_list('following', flat=True)
        # Return posts from those users
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

