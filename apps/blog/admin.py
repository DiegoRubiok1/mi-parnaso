"""
Admin configuration for the blog application.
"""
from django.contrib import admin

from .models import Post, PostComment, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin configuration for the Tag model."""
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin configuration for the Post model."""
    list_display = ("title", "author", "status", "published_at", "view_count")
    list_filter = ("status", "created_at", "published_at")
    search_fields = ("title", "author__username")
    readonly_fields = ("view_count", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)

    class Media:
        # pylint: disable=too-few-public-methods
        """Media classes."""
        css = {
            "all": (
                "https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.css",
            )}
        js = (
            "https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.js",
            "js/admin_easymde.js",
        )


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    """Admin configuration for Post comments."""
    list_display = ("post", "author", "created_at")
    list_filter = ("created_at",)
    search_fields = ("post__title", "author__username")
