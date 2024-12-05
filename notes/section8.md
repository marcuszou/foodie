# Section 8 Authentication and Authorization in Django

## Intro to Django Authorization - The User Object

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

## 8.2

## End of the Section