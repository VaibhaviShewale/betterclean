from django.contrib import admin
from .models import formdata
# Register your models here.


class displatData(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    
admin.site.register(formdata, displatData)