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

5- Visit http://127.0.0.1:8000/add-category it works but the form defined in `forms.py` does not show up. 

What's going on?  It seems needing more fine-tuning.

## 7.2 Deep Dive into Forms

It looks the `foordie_app/forms.py` bears some issue, the `forms.Form` , which is very generic, shall be replaced with `forms.modelForm`. 

Also from Django 5.1.0+, the `model` call must be defined in a `Meta` class: This heacahe took me 20 minutes to figure it out. Damn.

```python
from django import forms
from foodie_app.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        labels = {"name": "Category Name"}
```

Feel free to `inspect` via the browser while changing `form.as_p` to `form.as_div` in `add_category.html`.

Eventually we have upadted `foodie_app/views.py` a bit at `add_category` class:

```python
def add_category(request):
    if request.method == "POST":
        print(request.POST)
        form = CategoryForm(request.POST)
        context = {"form": form}
        return render(request, "foodie_app/index.html", context)
    else:
        form = CategoryForm
        context = {"form": form}
        return render(request, "foodie_app/add_category.html", context)
```

Also the `foodie_app/templates/foodie_app/add_category.html`:

```django
{% extends "base.html" %}
{% block content %}
    <h3>Add Category</h3>
    <div>
        <form method="post">
            {{ form.as_p}}
            <button type="submit">Submit</button>
        </form>
    </div>
{% endblock content %}
```

Then we give a go at http://127.0.0.1:8000/add-category, but it presents a "CSRF token missing" problem as below:

![csrf-issue](assets/7.2-1-csrf-issue.png)

Basically, Django is all about security in first place, which asks a CSRF token when posting any data into the backend database (Submitting a Category randomly may harm the database, DEFINITELY). Then we have to tune the form.py a bit as we are in dev environment.

```django
{% extends "base.html" %}
{% block content %}
    <h3>Add Category</h3>
    <div>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p}}
            <button type="submit">Submit</button>
        </form>
    </div>
{% endblock content %}
```

You should observe no issue now! Beautiful!

## 7.3 Form Validation - Save and Redirect

1- Basically modify `foodie_app/views.py` using `redirect` mothod:

```python
# foodie_app/views.py
from django.shortcuts import redirect, render

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
    if request.method == "POST":
        # print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foodie_app:index")
        else:
            context = {"form": form}
            return render(request, "foodie_app/add_category.html", context)
    else:
        form = CategoryForm
        context = {"form": form}
        return render(request, "foodie_app/add_category.html", context)
```

2- Optionally update `foodie_app/templates/foodie_app/index.html` a bit:

```django
{% extends "base.html" %}
{% block content %}
    <h3>Categories</h3>
    <div>
        <a href="{% url "foodie_app:add_category" %}">Add Category </a>
        {% for category in categories %}
            <div>
                <a href="{% url "foodie_app:recipes" category.id %}"> {{ category }} </a>
            </div>
        {% endfor %}
    </div>
{% endblock content %}
```

3- try to add a new category at http://127.0.0.1:8000/add-category

## 7.4 Custom Forms - Part 1

Go to `sandbox` playground.

1- Create a new `sandbox/forms.py`:

```python
# sandbox/forms.py
from django import forms

choices = [
    ('happy', 'Happy'),
    ("neutral", "Neutral"),
    ("sad", "Sad")
]

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    feedback = forms.CharField()
    satisfaction = forms.ChoiceField(choices)
```

2- Update `sandbox/models.py`:

```python
# sandbox/models.py
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    satisfaction = models.CharField(max_length=10)
```

3- Migrate the models in sandbox app:

```shell
python manage.py makemigrations sandbox
python manage.py migrate
```

4- Create a new `sandbox/templates/sandbox/feedback_form.html`:

```django
{% extends "base.html" %}
{% block content %}

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>

{% endblock content %}
```

5- Update `sandbox/urls.py`:

```python
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
```

6- Update `sandbox/views.py`:

```python
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # process the form
            print(form.cleaned_data)
            return redirect('thank_you')
        
    else:
        form = FeedbackForm()
        context = {"form": form}
        return render(request, "sandbox/feedbacK_form.html", context)
```

7- Will continue in next sub-section.

## 7.5 Custom Forms - Part 2

1- 









## End of the Section
