from django.contrib import admin
from django.db import models
from .models import *
# Register your models here.

class ReviewClass(admin.ModelAdmin):
    list_display = ('cfname', 'clname', 'crating', 'creview')

admin.site.register(MyReview)
admin.site.register(Profile)
admin.site.register(ReviewData, ReviewClass)