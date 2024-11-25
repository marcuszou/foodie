from random import choice
from django.http import HttpResponse
from django.shortcuts import render

fruits = [
    'mangoes',
    'pears',
    'oranges'
]
# Create your views here.
def index(request):
    data = choice(fruits)
    return HttpResponse(f"Hello there {data}")