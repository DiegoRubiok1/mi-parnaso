"""
Configuration for the about_me app.
"""
from django.apps import AppConfig


class AboutMeConfig(AppConfig):
    """
    App configuration for the about_me application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.about_me'
    label = 'about_me'
