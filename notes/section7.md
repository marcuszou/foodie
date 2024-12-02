# Section 7 - Django Forms and User Inputs



## 7.1 Django Forms and User Inputs - Introduction

Django abstracts out -

- Rendering HTML forms
- Data validation
- Data conversion

Django defines Forms as Classes.

- RecipeForm
- Add_CategoryForm
- ...

1- Create a `foodie_app/forms.py` :

```python
from django import forms
from foodie_app.models import Category

class CategoryForm(forms.Form):
    model = Category
    fields = ["name"]
    labels = {"name": "Category Name"}
```

2- Update `foodie_app/views.py`:

```python
# foodie_app/views.py
from django.shortcuts import render

from foodie_app.forms import CategoryForm
from .models import Category
from recipes.models import Recipe

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {"categories": categories}

    return render(request, "foodie_app/index.html", context)

def recipes(request, category_id):
    recipes = Recipe.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)

    context = {"recipes": recipes, "category": category}
    return render(request, "foodie_app/recipes.html", context)

def add_category(request):
    form = CategoryForm
    context = {"form": form}
    return render(request, "foodie_app/add_category.html", context)
```

3- Create a `foodie_app/templates/foodie_app/add_category.html` :

```django
{% extends "base.html" %}
{% block content %}
    <h3>Add Category</h3>
    <div>
        <form>
            {{ form.as_p}}
            
        </form>
    </div>
{% endblock content %}
```

4- Update `foodie_app/urls.py`:

```python
# foodie_app/urls.py
from django.urls import path
from . import views

app_name = "foodie_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/<int:category_id>/", views.recipes, name="recipes"),
    path("add-category/", views.add_category, name="Add_category")
]
```

5- Visit http://127.0.0.1:8000/add-category it works but needing more fine-tuning.



## 7.2 Showing all recipes in a Template



## End of the Section
