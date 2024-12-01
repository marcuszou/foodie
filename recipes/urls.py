# recipes/urls.py
from django.urls import path
from recipes import views

app_name = "recipes"
urlpatterns = [
    # Adding pattern name in the end of each path PLEASE,
    # as such, serving the calling from recipes.html.
    path("", views.recipes, name="index"),
    path("<int:recipe_id>", views.recipe, name="recipe_detail"),
]