from django.db import models

# Create your models here.

class Dataset (models.Model):
    name = models.CharField(max_length=40, blank= True)
    Data = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
