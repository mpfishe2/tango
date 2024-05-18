from django.urls import path
from .views import chat_view, submit_message_view

urlpatterns = [
    path("", chat_view, name="chat_view"),
    path("submit/", submit_message_view, name="submit_message")
]