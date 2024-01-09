# backend/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    # Add other user-related fields as needed

class ClothingItem(models.Model):
    name = models.CharField(max_length=255)
    # Add other clothing item fields as needed

class TryOnResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    result_image = models.ImageField(upload_to='try_on_results/')
    # Add other result-related fields as needed
