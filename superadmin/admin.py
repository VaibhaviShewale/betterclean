from django.contrib import admin

# Register your models here.
from .models import Services

class ServicesTable(admin.ModelAdmin):
    list_display = ('service_title', 'service_about')

admin.site.register(Services)