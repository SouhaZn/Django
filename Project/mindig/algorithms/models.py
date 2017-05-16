from __future__ import unicode_literals

from django.db import models

# Create your models here.

class algorithm (models.Model):
    name = models.CharField(max_length=40, blank= True)
    Code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class result (models.Model):
    name = models.CharField(max_length=40, blank= True)
    result = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
