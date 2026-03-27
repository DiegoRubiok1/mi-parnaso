from django.shortcuts import render

from apps.blog.models import Post


def home_view(request):
	latest_posts = Post.objects.filter(status="published").order_by("-published_at")[:5]
	context = {"latest_posts": latest_posts}
	return render(request, "core/home.html", context)
