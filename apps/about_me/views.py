"""
Views for the about_me app.
"""
from django.shortcuts import render


def about_me(request):
    """About me page view"""
    return render(request, "about_me/about_me.html")
