from django.contrib import admin
from bookshelf.models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff"]

