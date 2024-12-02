from django import forms
from foodie_app.models import Category

class CategoryForm(forms.Form):
    model = Category
    fields = ["name"]
    labels = {"name": "Category Name"}
