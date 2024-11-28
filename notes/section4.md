# Section 4 - Django Models, Database, ORM & Migrations

## 

## 4.1 Intro to Django Models

![intro-Models](assets/4.1-1-Intro-to-Models.png)

![intro-Models](assets/4.1-2-Intro-to-Models.png)



## 4.2 Models and Relationships

![](assets/4.2-1-Model.png)

**Model**: A single, definitive source of information about your data

        Examples: Recipe, Categoty, Address, etc...

![](assets/4.2-2-Model-Relationships.png)



## 4.3 Restructure Code - Creating the Foodie App

```shell
python manage.py startapp foodie_app
```

then create/change the contents of `foodie_app/urls.py`

```python
from django.urls import path
from . import views

app_name = "foodie_app"
urlpatterns = [
    path("", views.index)
]
```

The `foodie_app/views.py`

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "foodie_app/index.html")
```

and the `foodie_app/templates/foodie_app/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Foodie_app</title>
</head>
<body>
    <p>Foodie_App</p>
</body>
</html>
```

finally add " 'foodie_app', " to `foodie/settings.py`.

## 4.3 Restructuring base.html

1- Move the `sandbox/templates/sandbox/base.html` to `templates/base.html`

2- Modify `foodie/settings.py: TEMPLATES --> "DIRS": [BASE_DIR / 'templates' ] 

3- Modify the `foodie_app/templates/foodie_app/index.html`

