from django.contrib import admin
from Data.models import Dataset

class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'Data')
    list_filter =('created_at', 'updated_at')
    search_fields = ['name']
    class meta:
        model = Dataset

admin.site.register(Dataset, DatasetAdmin)
