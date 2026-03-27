from django.conf import settings
from django.db import models
from django.utils.text import slugify


class ForumThread(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="forum_threads")
	content = models.TextField()
	is_locked = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at"]

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.title

	def reply_count(self) -> int:
		return self.replies.count()


class ForumReply(models.Model):
	thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE, related_name="replies")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="forum_replies")
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["created_at"]

	def __str__(self) -> str:
		return f"Respuesta de {self.author} en {self.thread}"
