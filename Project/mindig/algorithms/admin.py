from django.contrib import admin
from algorithms.models import algorithm, result
# Register your models here.

class AlgorithmAdmin(admin.ModelAdmin):
    list_filter =('created_at', 'updated_at')
    search_fields = ['name']
    class meta:
        model = algorithm

admin.site.register(algorithm, AlgorithmAdmin)
admin.site.register(result)
