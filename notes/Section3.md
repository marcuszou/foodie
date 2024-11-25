# Section 3 - Django Fundamentals - Deep Dive

## 3.1 Initial Setup
1- Install Python 3.12 and Update pip to latest version
```shell
# Go to www.python.org to download the installer files
# Then install Python 3.12.3 for macOS/Linux/Windows

# Upgrade pip to latest version for the Host 
python3 -m pip install --upgrade pip  ## macOS and Linux
python -m pip install --upgrade pip   ## Windows
```
2- Create a project folder and create/activate the virtual Env
```shell
mkdir foodie
cd foodie

python -m venv venv
venv/bin/activate        ## macOS, Linux
./venv/scripts/activate  ## Windows

# Upgrade pip to latest version for the Venv 
python3 -m pip install --upgrade pip  ## macOS and Linux
python -m pip install --upgrade pip   ## Windows
```
3- Install Django and Create project
```shell
pip install django
django-admin startproject foodie .
```

## 3.2 - Django Project File Structure

## 3.3 Apps and Running up the Server
1- Start a sandbox app
```shell
django-admin startapp sandbox
```
2- Initial running up the server
```shell
python manage.py runserver
```
3- add more routes
```shell
## Create a urls.py in sandbox folder
touch sandbox/urls.py
```
4- edit the sandbox/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index)
]
```
5- edit sandbox/views.py
```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")
```
6- Import the urls of sandbox to foodie/urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sandbox/', include('sandbox.urls')),
]
```
7- add the app (sandbox) to foodie/settings.py
```python
INSTALLED_APPS = [
    # my apps
    'sandbox',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
8- Go to http://127.0.0.1:8000/sandbox to try
