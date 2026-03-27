from django.contrib import admin

from .models import Post, PostComment, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ("name", "slug")
	prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "status", "published_at", "view_count")
	list_filter = ("status", "created_at", "published_at")
	search_fields = ("title", "author__username")
	readonly_fields = ("view_count", "created_at", "updated_at")
	prepopulated_fields = {"slug": ("title",)}
	filter_horizontal = ("tags",)


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
	list_display = ("post", "author", "created_at")
	list_filter = ("created_at",)
	search_fields = ("post__title", "author__username")

