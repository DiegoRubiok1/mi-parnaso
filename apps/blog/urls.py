from django.urls import path

from .views import PostDetailView, PostListView, add_comment_view

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("<slug:slug>/comment/", add_comment_view, name="add-comment"),
]

