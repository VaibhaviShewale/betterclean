from django.contrib import admin
from .models import formdata
# Register your models here.

class displatData(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'message', 'status')
    fields = (('name', 'email'), ('message'), ('status'), ('staff'), ('remark'))
    list_display = ('name', 'message', 'status', 'staff')
    list_filter = ('status',)

    def get_queryset(self, request):
        qs = super(displatData, self).get_queryset(request)
        if request.user.is_superuser == False:
            pass
        else:
            return qs.all()
        return qs.filter(staff=request.user)
            

    def save_model(self, request, obj, form, change):
        if obj.remark:
            obj.status = "completed"
        elif obj.staff:
            obj.status = "processing"
        else:
            obj.status = "pending"
        super().save_model(request, obj, form, change)
    
admin.site.register(formdata, displatData)