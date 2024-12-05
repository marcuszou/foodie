from django.urls import path, include
from .views import register

urlpatterns = [
    path("register/", register, name="regiser"),
    path("accounts/", include("django.contrib.auth.urls"))
]