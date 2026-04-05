"""
Database models for the blog application.
"""
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
import markdown


class Tag(models.Model):
    """Model representing a tag for blog posts."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)


class Post(models.Model):
    """Model representing a blog post."""
    STATUS_CHOICES = [
        ("draft", "Borrador"),
        ("published", "Publicado"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts")
    content_md = models.TextField()
    content_html = models.TextField(blank=True)
    featured_image = models.ImageField(
        upload_to="featured_images/", blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft")
    published_at = models.DateTimeField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    class Meta:
        """Meta options for Post model."""
        # pylint: disable=too-few-public-methods
        ordering = ["-published_at", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.content_html = markdown.markdown(
            str(self.content_md))  # Convierte Markdown a HTML
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.title)

    def is_published(self) -> bool:
        """Check if the post is published."""
        return self.status == "published" and self.published_at is not None


class PostComment(models.Model):
    """Model representing a comment on a blog post."""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for PostComment model."""
        # pylint: disable=too-few-public-methods
        ordering = ["created_at"]

    def __str__(self) -> str:
        return str(f"Comentario de {self.author} en {self.post}")


@receiver(post_save, sender=Post)
def notify_subscribers_new_post(sender, instance, created, **kwargs):  # pylint: disable=unused-argument
    """
    Notify subscribers via email when a new post is published.
    """
    if created and instance.status == "published":
        # pylint: disable=import-outside-toplevel
        from apps.accounts.models import Profile

        # pylint: disable=no-member
        subscribers = Profile.objects.filter(
            subscribe_to_blog=True, user__is_active=True
        ).select_related("user")
        recipient_list = [p.user.email for p in subscribers if p.user.email]

        if recipient_list:
            post_url = reverse(
                "blog:post-detail",
                kwargs={
                    "slug": instance.slug})
            if hasattr(settings, "SITE_URL") and settings.SITE_URL:
                full_url = f"{settings.SITE_URL.rstrip('/')}{post_url}"
            else:
                full_url = f"https://miparnaso.com{post_url}"

            subject = f"Nuevo artculo en Mi Parnaso: {instance.title}"
            message = (
                f"Hola,\n\n"
                f"Carmen ha publicado un nuevo artculo: '{instance.title}'.\n\n"
                f"Puedes leerlo aqu: {full_url}\n\n"
                f"--- \n"
                f"Has recibido este correo porque ests suscrito a las novedades del blog."
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
