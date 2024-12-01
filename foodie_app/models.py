# foodie_app/models.py
from django.db import models

# Create Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
