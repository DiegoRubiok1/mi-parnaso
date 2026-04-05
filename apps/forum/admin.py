"""
Forum admin configuration.
"""
from django.contrib import admin

from .models import ForumReply, ForumThread


@admin.register(ForumThread)
class ForumThreadAdmin(admin.ModelAdmin):
    """Admin view for ForumThread."""
    list_display = ("title", "author", "created_at", "is_locked")
    list_filter = ("created_at", "is_locked")
    search_fields = ("title", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")


@admin.register(ForumReply)
class ForumReplyAdmin(admin.ModelAdmin):
    """Admin view for ForumReply."""
    list_display = ("thread", "author", "created_at")
    list_filter = ("created_at",)
    search_fields = ("thread__title", "author__username")
