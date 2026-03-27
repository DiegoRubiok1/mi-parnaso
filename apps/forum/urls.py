from django.urls import path

from .views import (
    ForumThreadDetailView,
    ForumThreadListView,
    add_reply_view,
    create_thread_view,
)

app_name = "forum"

urlpatterns = [
    path("", ForumThreadListView.as_view(), name="thread-list"),
    path("create/", create_thread_view, name="create-thread"),
    path("<slug:slug>/", ForumThreadDetailView.as_view(), name="thread-detail"),
    path("<slug:slug>/reply/", add_reply_view, name="add-reply"),
]

