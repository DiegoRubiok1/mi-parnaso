"""
Database models for the forum application.
"""
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class ForumThread(models.Model):
    """Model representing a thread in the forum."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="forum_threads")
    content = models.TextField()
    is_locked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for ForumThread."""
        # pylint: disable=too-few-public-methods
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.title)

    def reply_count(self) -> int:
        """Returns the number of replies the thread has."""
        # pylint: disable=no-member
        return self.replies.count()


class ForumReply(models.Model):
    """Model representing a reply to a forum thread."""
    thread = models.ForeignKey(
        ForumThread,
        on_delete=models.CASCADE,
        related_name="replies")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="forum_replies")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for ForumReply."""
        # pylint: disable=too-few-public-methods
        ordering = ["created_at"]

    def __str__(self) -> str:
        return str(f"Respuesta de {self.author} en {self.thread}")


@receiver(post_save, sender=ForumThread)
def notify_subscribers_new_thread(sender, instance, created, **kwargs):  # pylint: disable=unused-argument
    """
    Notify subscribers via email when a new thread is created in the forum.
    """
    if created:
        # pylint: disable=import-outside-toplevel
        from apps.accounts.models import Profile

        # pylint: disable=no-member
        subscribers = Profile.objects.filter(
            subscribe_to_forum=True, user__is_active=True
        ).select_related("user")
        recipient_list = [p.user.email for p in subscribers if p.user.email]

        if recipient_list:
            thread_url = reverse(
                "forum:thread-detail",
                kwargs={
                    "slug": instance.slug})
            if hasattr(settings, "SITE_URL") and settings.SITE_URL:
                full_url = f"{settings.SITE_URL.rstrip('/')}{thread_url}"
            else:
                full_url = f"https://miparnaso.com{thread_url}"

            subject = f"Nuevo tema en el foro de Mi Parnaso: {instance.title}"
            message = (
                f"Hola,\n\n"
                f"{instance.author.username} ha abierto un nuevo tema en el foro: "
                f"'{instance.title}'.\n\n"
                f"Puedes participar aqu: {full_url}\n\n"
                f"--- \n"
                f"Has recibido este correo porque ests suscrito a las novedades del foro."
            )

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    recipient_list,
                    fail_silently=True,
                )
            except Exception:  # pylint: disable=broad-exception-caught
                pass
