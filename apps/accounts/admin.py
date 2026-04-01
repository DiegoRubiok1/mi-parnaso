"""
Admin configuration for the accounts app.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BanLog, Profile, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom user admin for the accounts app.
    """
    fieldsets = UserAdmin.fieldsets + (("Moderacion", {"fields": ("is_banned",)}),)
    list_display = ("username", "email", "is_staff", "is_active", "is_banned")
    list_filter = ("is_staff", "is_active", "is_banned")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile admin for the accounts app.
    """
    list_display = ("user",)


@admin.register(BanLog)
class BanLogAdmin(admin.ModelAdmin):
    """
    Ban log admin for the accounts app.
    """
    list_display = ("user", "created_by", "created_at")
    search_fields = ("user__username", "reason")
