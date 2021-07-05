from django import forms
from django.db import models
from django.contrib.auth.models import User
from candidates.models import Candidate


STATUS_PENDING = 'pending'
STATUS_REJECTED = 'rejected'
STATUS_ACCEPTED = 'accepted'
STATUS_CHOICE = (
    (STATUS_PENDING,'Pending'),
    (STATUS_REJECTED, 'Rejected'),
    (STATUS_ACCEPTED, 'Accepted'),
)

# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length = 100, verbose_name= "Job Name")
    job_desc =  models.TextField(verbose_name="Job Description")
    min_age =  models.IntegerField(verbose_name="Minimum Age")
    max_age =  models.IntegerField(verbose_name="Maximum Age")
    salary =  models.IntegerField(verbose_name="Salary")
    n_openings =  models.IntegerField(verbose_name="Number of Openings")
    creator =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Client")
    
    def __str__(self):
        return self.job_name
        
    
class JobApplied(models.Model):
    username = models.ForeignKey(User, verbose_name="User Name", on_delete=models.CASCADE)
    job_applied = models.ForeignKey(Job, verbose_name="Job Applied For", on_delete=models.CASCADE)
    status =  models.CharField(max_length=50,choices= STATUS_CHOICE, default= STATUS_PENDING)
    def __str__(self):
        return (self.username.username)