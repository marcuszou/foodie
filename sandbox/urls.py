# sandbox/urls.py
from django.urls import path
from . import views

app_name = "sandbox"
urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/<int:pk>", views.RecipeDetailView.as_view(), name="recipeDetail"),
    path("refreshing/", views.SpecificRecipesView.as_view(), name="refreshing_recipes"),
    path("feedback/", views.feedback, name ="feedback")
]
