"""
App configuration for the accounts application.
"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the accounts application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    label = 'accounts'
