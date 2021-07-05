from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import RadioSelect

USER_CANDIDATE='candidate'
USER_REC= 'recruiter'
USER_CHOICE=(
    (USER_CANDIDATE,'Candidate'),
    (USER_REC, 'Recruiter'),
)
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Your username should be unique one'})
    ,required=True,max_length=30)
    password1=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Password should be more than 8 characters'})
    ,required=True,max_length=30)
    password2= forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Type the password as same as above'})
    ,required=True,max_length=30)
    usertype = forms.ChoiceField(choices=USER_CHOICE)
    class meta:
        fields = "__all__"
    