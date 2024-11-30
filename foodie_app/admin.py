from django.contrib import admin
from .models import Category, Recipe

# Customize the display in admin site
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")
    search_fields = ["name"]

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")
    search_fields = ["name"]

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)