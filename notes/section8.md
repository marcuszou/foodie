# Section 8 - Authentication and Authorization in Django



## 8.1 Intro to Django Authorization - The User Object

Users Accounts:

- Groups
- Permissions
- Sessions

The user model

- Username
- Password
- last_active
- first_name
- last_name

Open "SQLITE EXPLORER" in VS Code looking into the data tables of:

- auth_group
- auth_group_permissions
- auth_user
- auth_user_groups
- ...

Then run (click the triangle) the `auth_user` data table to take a look at the `admin` user (at least one user).

A direct user interface can be found at http://127.0.0.1:8000/admin at the `AUTHENTICATION AND AUTHORIZATION` part.
Feel free to add a user in the ADMIN website.

Another way to manage the user and group is through `Django Shell`: It's actually Python env.

```shell
python manage.py shell
```

Then run a few commands as below:

```python
## Import the module
from django.contrib.auth.models import User
users = User.objects.all()

## You should have 2 users listed if you have created a new user "James Bond" previously
for user in users:
    print(user, user.id)

## Create a new user from here
user = User.objects.create_user("John", "jdoe@google.com", "jd@password")

## Add the lastname for the new user
user.first_name = "John"
user.last_name = "Doe"
user.save()

## Exit the shell
exit()
```

Actually we can populate the username into our Homepage by adding a line of 

```django
{{ user.username }}
```

into the `templates/base.html` file:

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>foodie</title>
</head>
<body>
    <nav>
        <div>
            <a href="{% url "foodie_app:index" %}"> Foodie </a>
            <a href="{% url "foodie_app:add_recipe_no_genre" %}"> Add Recipe </a>
            {{ user.username }}
        </div>
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

then visit the home page to take a look.



## 8.2 Creating User Registration Component - Part 1

1- Create a new app: `accounts`

```shell
python manage.py startapp accounts
```

2- Register the app in `foodie/settings.py`.

3- Update `accounts/urls.py`:

```python
from django.urls import path, include
from .views import register

urlpatterns = [
    path("register/", register, name="regiser"),
    path("accounts/", include("django.contrib.auth.urls"))
]
```

4- Update `accounts/views.py`:

```python
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in
            login(request, new_user)
            return HttpResponse("Yay! User Created!")
    context = {"form": form}
    return render(request, "registration/regiser.html", context)
```

## 8.3 Register a User Successfully

1- Create `accounts/templates/registration/register.html`:

```django
{% extends "base.html" %}
{% block content %}
    <h3>Register
    </h3>
    <div>
        <form action="{% url "accounts:register" %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Register</button>
        </form>
    </div>
{% endblock content %}
```

2- Update `accounts/urls.py`:

```python
from django.urls import path, include
from .views import register

app_name = "accounts"
urlpatterns = [
    path("register/", register, name="regiser"),
    path("accounts/", include("django.contrib.auth.urls"))
]
```

3- Also add the path in `foodie/urls.py`:

```python
    path('accounts/', include('accounts.urls'))
```

4- Give  try at http://127.0.0.1:8000/accounts/register

Issue ....



## End of the Section