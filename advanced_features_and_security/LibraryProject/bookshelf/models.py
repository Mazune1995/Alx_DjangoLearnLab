from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Add any extra fields here if needed.
    """
    # Example extra field (optional)
    # phone_number = models.CharField(max_length=15, blank=True, null=True)
    pass
# Custom User Model
class CustomUser(AbstractUser):
    pass

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

