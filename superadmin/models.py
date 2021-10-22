from django.db import models

# Create your models here.

class Services(models.Model):
    service_title = models.CharField(max_length=100, verbose_name="Title")
    service_about = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name_plural = "Services"