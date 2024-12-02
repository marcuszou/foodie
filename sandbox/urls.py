# sandbox/urls.py
from django.urls import path
from . import views

app_name = "sandbox"
urlpatterns = [
    path("", views.index, name="index"),
    path('recipes/', views.RecipeListView.as_view(), name="recipes_list")
]
