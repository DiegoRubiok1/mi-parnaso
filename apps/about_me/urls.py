"""
URL configuration for the about_me app.
"""
from django.urls import path

from .views import about_me

APP_NAME = "about_me"

urlpatterns = [
    path("about_me/", about_me, name="about_me")
]
