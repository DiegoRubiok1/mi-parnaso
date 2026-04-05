"""
Forum application configuration.
"""
from django.apps import AppConfig


class ForumConfig(AppConfig):
    """Configuration class for the forum app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.forum'
    label = 'forum'
