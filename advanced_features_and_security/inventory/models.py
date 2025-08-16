from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view product"),
            ("can_create", "Can create product"),
            ("can_edit", "Can edit product"),
            ("can_delete", "Can delete product"),
        ]

    def __str__(self):
        return self.name

