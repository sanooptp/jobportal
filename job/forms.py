# import form class from django
from django import forms
from django.db import models
from django.db.models import fields

# import GeeksModel from models.py
from .models import Job, JobApplied

# create a ModelForm
class JobForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Job
		fields = "__all__"
		exclude = ['creator']
