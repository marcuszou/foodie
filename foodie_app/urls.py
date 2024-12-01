# foodie_app/urls.py
from django.urls import path
from . import views

app_name = "foodie_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/<int:category_id>/", views.recipes, name="recipes")
]
