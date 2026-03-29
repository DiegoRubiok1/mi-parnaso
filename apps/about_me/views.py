from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages


def about_me(request):
    """About me page view"""
    return render(request, "about_me/about_me.html")
