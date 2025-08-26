from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Self-referential ManyToMany for following system
    following = models.ManyToManyField(
        "self",
        symmetrical=False,           # following is not mutual by default
        related_name="followers",
        blank=True
    )

    def __str__(self):
        return self.username

