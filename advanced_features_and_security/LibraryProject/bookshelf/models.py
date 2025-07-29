from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateField(default='2024-01-01')


    def __str__(self):
        return self.title

