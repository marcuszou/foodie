# Section 6 - Django Templates amd Static Files

## 6.1 Creating the base.html template, Navbar and Footer

1- Update the `templates/base.html` :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>foodie</title>
</head>
<body>
    <nav>
        <div>Foodie</div>
    </nav>
    <main>
        <div class="container">
            {% block content %}
            {% endblock content %}
        </div>
    </main>
    <div>
        <hr>
        <footer>
            <pre>Footer</pre>
        </footer>
    </div>
</body>
</html>
```

2- Create the `recipes/templates/recipes/recipes.html` file:

```django
{% extends "base.html" %}
{% block content %}
    All recipes go here!
{% endblock content %}
```

3- Update the `recipes/views.py` file:

```python
# recipes/views.py
from django.http import HttpResponse
from django.shortcuts import render
from recipes.models import Recipe
from django.db.models import Avg, Count, Sum, Max, Min
from django.db.models import Q

# Create your views here.
def recipes(request):

    recipes = Recipe.objects.filter(name__contains="Mojito").exists()

    return render(request, "recipes/recipes.html")
```

4- Test out http://127.0.0.1:8000/recipes/ and http://127.0.0.1:8000/, they should have same interface as of now.

## 6.2 Showing all recipes in a Template

Change the `recipes/views.py`:

```python
# recipes/views.py
from django.shortcuts import render
from recipes.models import Recipe

# Create your views here.
def recipes(request):

    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    return render(request, "recipes/recipes.html", context)
```

then update the `recipes/templates/recipes/recipes.html`:

```django
{% extends "base.html" %}
{% block content %}
    <div>
        {% for recipe in recipes %}
        <div>
            <h5> {{ recipe.name }} </h5>
            <p> {{ recipe.description }} </p>
        </div>
        {% endfor %}
    </div>

{% endblock content %}
```

## 6.3 Showing the Recipes in the Details Template

Change the `recipes/urls.py`:

```python
# recipes/urls.py
from django.urls import path
from recipes import views

app_name = "recipes"
urlpatterns = [
    path("", views.recipes),
    path("<int:recipe_id>", views.recipe)
]
```

Update the `recipes/views.py`:

```python
# recipes/views.py
from django.shortcuts import render
from recipes.models import Recipe

# Create your views here.
def recipes(request):

    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    return render(request, "recipes/recipes.html", context)

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        "recipe": recipe
    }

    return render(request, "recipes/recipe.html", context)
```

Create a detailed recipe html: `recipes/templates/recipes/recipe.html`:

```django
{% extends "base.html" %}
{% block content %}
    <div>
        <div>
            <h5> {{ recipe.name }} </h5>
        </div>
    </div>

{% endblock content %}
```

then visit: http:/127.0.0.1:8000/recipes/3 for a lokk.



## 6.4



## End of the Section
