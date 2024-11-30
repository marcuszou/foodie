# comments/urls.py
from django.urls import path
from comments import views

app_name = "comments"
urlpatterns = [
    path("", views.comments)
]