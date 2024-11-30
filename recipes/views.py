# recipes/views.py
from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe

# Create your views here.
def recipes(request):
    # recipes = Recipe.objects.filter(category__name__iexact="salad")
    # recipes = Recipe.objects.exclude(name__contains="Chocolate")
    recipes = Recipe.objects.filter(category__name__iexact="Soup").exclude(name__contains="chocolate").order_by("-date_added")
    print("Recipes", recipes)
    return HttpResponse("Hello from Recipes")