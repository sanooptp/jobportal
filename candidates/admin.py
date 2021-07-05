from django.contrib import admin
from .models import Candidate

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    # exclude = ('c_username',)
    list_display = ('c_username',)

    # def save_model(self, request, obj, form, change):
        # obj.c_username =  request.user
        # obj.save()
    
    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Candidate.objects.all()
        else:
            return Candidate.objects.filter(c_username=request.user)



admin.site.register(Candidate, CandidateAdmin)
