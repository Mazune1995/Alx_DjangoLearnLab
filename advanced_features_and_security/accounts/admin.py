from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Make sure you're importing, NOT defining

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass  # You can customize the admin as needed

