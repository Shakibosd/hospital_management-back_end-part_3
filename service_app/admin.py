from django.contrib import admin
from .models import Services

class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']
admin.site.register(Services, ServicesModelAdmin)
