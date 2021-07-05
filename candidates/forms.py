# import form class from django
from django import forms
from django.forms.fields import CharField
from job.models import JobApplied
from django.contrib.auth.models import User

# import GeeksModel from models.py
from .models import Candidate

# create a ModelForm
class CandidateForm(forms.ModelForm):
	# # specify the name of model to use
	# name=forms.CharField(widget=forms.TextInput(
	# attrs={'class':'form-control'	})
	# ,required=True,max_length=30)
	# age= forms.IntegerField(widget=forms.TextInput(
	# attrs={'class':'form-control'	}), required=True)

	class Meta:
		model = Candidate
		fields = "__all__"
		exclude = ['c_username']
		

class JobApplyForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = JobApplied
		fields = "__all__"
		exclude =['username','candidate','job_applied', 'status']
		