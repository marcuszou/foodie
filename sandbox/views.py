# from random import choice
from django.http import HttpResponse
from django.shortcuts import render

dataset = {"name": "Marcus", "age": 123}
context1 = {"data": dataset}

foodset = ["Pizza", "Pasta", "Salad", "Bread"]
context = {"foods": foodset}
# Create your views here.
def index(request):
    return render(request, "sandbox/index.html", context)