# Section 5 - Django QuerySet API



## 5.1 Django QuerySet API - Overview

QuerySet:

- Collection of Database queries

- Lazily Evaluated

  

![queryset](assets/5.1-1-QuerySet-Overview.png)

Then modify the `recipes/views.py` :

```python
# recipes/views.py
from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe

# Create your views here.
def recipes(request):
    recipes = Recipe.objects.all()
    print("Recipes", recipes)
    
    return HttpResponse("Hello from Recipes")
```

Open http://127.0.0.1:8000/recipes/. the query set results shall show up in the terminal.

There are a few methods:

​	.all()

​	.first()

​	.get(pk=4)

​	.get(id=1)



## 5.2 QuerySet API - Using filter with contains & exact Field Lookups

**Method**: .filter(category="Salad")

But `recipes = Recipe.objects.filter(category="Salad")` will cause issue, because `category` is actually a foreign key from `Categoty` module. Then we need to change to `category__name__exact="Salad"` or `category__name__iexact="Salad"`.

```python
# recipes/views.py
from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe

# Create your views here.
def recipes(request):
    recipes = Recipe.objects.filter(category__name__iexact="salad")
    print("Recipes", recipes)
    return HttpResponse("Hello from Recipes")
```

Another filter option is `filter(category__name__icontains="Salad another")`.



## 5.3 QuerySet API - Using the exclude Type

Method:`.exclude(name__contains="Soup")`

```python
# recipes/views.py
from django.http import HttpResponse
from django.shortcuts import render
from recipes.models import Recipe

# Create your views here.
def recipes(request):
    # recipes = Recipe.objects.filter(category__name__iexact="Soup")
    recipes = Recipe.objects.exclude(name__contains="Chocolate")
    print("Recipes", recipes)
    return HttpResponse("Hello from Recipes"):
```



## 5.4 QuerySet API - Filter Chaining

1- Method changed to:

```python
## Filter Chaining with order_by
## `-` means descending.
recipes = Recipe.objects.filter(category__name__iexact="Soup").exclude(name__contains="Chocolate").order_by("-date_added")
```



2- Modify `foodie/settings.py: TEMPLATES --> 

```
"DIRS": [BASE_DIR / 'templates' ] 
```

3- Modify the `foodie_app/templates/foodie_app/index.html`

```django
{% extends "base.html" %}
{% block content %}
    Hello there from Foodie App!
{% endblock content %}
```





## End of the Section
