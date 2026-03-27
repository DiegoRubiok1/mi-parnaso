from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.name


class Post(models.Model):
	STATUS_CHOICES = [
		("draft", "Borrador"),
		("published", "Publicado"),
	]

	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
	content_md = models.TextField()
	content_html = models.TextField(blank=True)
	featured_image = models.ImageField(upload_to="featured_images/", blank=True, null=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
	published_at = models.DateTimeField(blank=True, null=True)
	view_count = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

	class Meta:
		ordering = ["-published_at", "-created_at"]

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.title

	def is_published(self) -> bool:
		return self.status == "published" and self.published_at is not None


class PostComment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_comments")
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["created_at"]

	def __str__(self) -> str:
		return f"Comentario de {self.author} en {self.post}"
