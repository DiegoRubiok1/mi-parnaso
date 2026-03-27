from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
	email = models.EmailField(unique=True)
	is_banned = models.BooleanField(default=False)

	def __str__(self) -> str:
		return self.username


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
	photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True)

	def __str__(self) -> str:
		return f"Perfil de {self.user.username}"


class BanLog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ban_logs")
	reason = models.TextField(blank=True)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name="created_ban_logs",
	)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance: User, created: bool, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	else:
		Profile.objects.get_or_create(user=instance)
