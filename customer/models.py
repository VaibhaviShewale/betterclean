from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)    
    img = models.ImageField(upload_to='profiles/', default='profiles/avatar.png')

class ReviewData(models.Model):
    cfname = models.CharField(max_length=20)
    clname = models.CharField(max_length=20)
    ccity = models.CharField(max_length=100)
    crating = models.SmallIntegerField()
    creview = models.TextField()

class MyReview(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    rating = models.SmallIntegerField()
    review = models.TextField()