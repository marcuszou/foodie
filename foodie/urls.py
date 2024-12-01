# foodie/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sandbox/', include('sandbox.urls')),
    path('',  include('foodie_app.urls')),
    path('recipes/', include('recipes.urls')),
    path('comments/', include('comments.urls')),
]
