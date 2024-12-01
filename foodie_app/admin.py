# foodie_app/admin.py
from django.contrib import admin
from .models import Category

# Customize the display in admin site
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")
    search_fields = ["name"]

# Register your models here.
admin.site.register(Category, CategoryAdmin)
