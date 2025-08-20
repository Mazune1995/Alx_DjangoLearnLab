# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Users can follow other users
    following = models.ManyToManyField(
        "self",
        symmetrical=False,   # following ≠ follower
        related_name="followers",
        through="UserFollow",
    )

class UserFollow(models.Model):
    follower = models.ForeignKey(
        CustomUser,
        related_name="following_relations",
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        CustomUser,
        related_name="follower_relations",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")

