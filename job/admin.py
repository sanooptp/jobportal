from django.contrib import admin
from .models import Job, JobApplied


class JobAdmin(admin.ModelAdmin):
    # exclude = ('creator',)
    list_display = ('job_name','creator',)

    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creator=request.user)

    def get_list_display(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return ('job_name','creator',)
        else:
            return ('job_name',)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

# customizing access to JobApplied Model    
class JobApplyAdmin(admin.ModelAdmin):
    list_display = ('username','job_applied',)
    # exclude = ('username',)

    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return JobApplied.objects.all()
        else:
            return JobApplied.objects.filter(username=request.user)

    # def save_model(self,request,obj,form,change):
    #     obj.username =  request.user
    #     obj.save()

admin.site.register(Job, JobAdmin)
admin.site.register(JobApplied, JobApplyAdmin)

# Register your models here.
