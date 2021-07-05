from django.db import models
from django.contrib.auth.models import User


GENDER_MALE= 'Male'
GENDER_FEMALE= 'Female'
GENDER_OTHERS= 'Others'
GENDER_CHOICE=(
    (GENDER_MALE,'Male'),
    (GENDER_FEMALE, 'Female'),
    (GENDER_OTHERS, 'Others'),
    
)
STATUS_PENDING = 'Pending'
STATUS_REJECTED = 'Rejected'
STATUS_ACCEPTED = 'Accepted'
STATUS_CHOICE = (
    (STATUS_PENDING,'Pending'),
    (STATUS_REJECTED, 'Rejected'),
    (STATUS_ACCEPTED, 'Accepted'),
)
# Create your models here.
class Candidate(models.Model):
    name =  models.CharField(max_length= 100)
    age =  models.IntegerField()
    gender =  models.CharField(max_length= 20, choices= GENDER_CHOICE, default= GENDER_FEMALE)
    mobile =  models.CharField(max_length= 10)
    city = models.CharField(max_length= 100)
    exp_salary = models.IntegerField()
    relocate = models.BooleanField(default=False)
    c_username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Username")
    resume = models.FileField(default = None, upload_to=None, max_length=100)
    def __str__(self):
        return self.name

