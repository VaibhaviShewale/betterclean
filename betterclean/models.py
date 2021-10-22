from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
    ('pending', "PENDING"),("processing","PROCESSING"),("completed","COMPLETED")
)

class formdata(models.Model):
    name = models.CharField(max_length=50, verbose_name="Customer name")
    email = models.EmailField(verbose_name="Email ID")
    phone = models.CharField(max_length=12,verbose_name="Phone")
    message = models.TextField(verbose_name="Query")

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending",verbose_name="Status")
    remark = models.TextField(blank=True, verbose_name="Remark")
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,limit_choices_to={'is_staff':True,'is_active':True, 'is_superuser':False}, verbose_name="Staff")

    class Meta:
        verbose_name = "Query"
        verbose_name_plural = "Customer queries"

