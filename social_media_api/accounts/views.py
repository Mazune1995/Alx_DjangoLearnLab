from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer
from .models import CustomUser, UserFollow   # ✅ import your models here


class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        follow, created = UserFollow.objects.get_or_create(
            follower=request.user,
            following=target_user
        )

        if created:
            return Response(
                {"detail": f"You are now following {target_user.username}."},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"detail": f"You already follow {target_user.username}."},
                status=status.HTTP_200_OK
            )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        deleted, _ = UserFollow.objects.filter(
            follower=request.user,
            following=target_user
        ).delete()

        if deleted:
            return Response(
                {"detail": f"You unfollowed {target_user.username}."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": f"You were not following {target_user.username}."},
                status=status.HTTP_400_BAD_REQUEST
            )

