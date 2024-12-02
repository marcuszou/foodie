# sandbox/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from recipes.models import Recipe

# Function based View
## data = ["Pizza", "Pasta", "Salad", "Bread"]
## context = {"foods", data}
data = Recipe.objects.all()
context = {"recipes": data}
# Create your views here.
def index(request):
    return render(request, "sandbox/index.html", context)

# Class-based View
class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/index.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "sandbox/recipeDetail.html"
    context_object_name = "recipe"
