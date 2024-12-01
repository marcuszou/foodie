# recipes/views.py
from django.http import HttpResponse
from django.shortcuts import render
from recipes.models import Recipe
from django.db.models import Avg, Count, Sum, Max, Min
from django.db.models import Q

# Create your views here.
def recipes(request):
    # recipes = Recipe.objects.all()
    # recipes = Recipe.objects.filter(category__name__iexact="salad")
    # recipes = Recipe.objects.exclude(name__contains="Chocolate")
    # recipes = Recipe.objects.filter(category__name__iexact="Soup").exclude(name__contains="chocolate").order_by("-date_added")
    # recipes = Recipe.objects.all()[:3]
    # recipes = Recipe.objects.aggregate(Count("id"))
    # recipes = Recipe.objects.filter(id__gt=3)
    # recipes = Recipe.objects.filter(Q(name__startswith="M") | Q(description__icontains="lava"))
    recipes = Recipe.objects.filter(id__gt=3).values()
    # recipes = Recipe.objects.filter(id__gt=3).values_list()
    # recipes = Recipe.objects.filter(id__gt=3).count()
    recipes = Recipe.objects.filter(name__contains="Mojito").exists()

    print("Recipes", recipes)
    return HttpResponse("Hello from Recipes")