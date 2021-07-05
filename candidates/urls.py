from django.urls import path,include
from .views import CandidateView, JobDetails, save, CandidateShowView
from job.views import JobList
urlpatterns = [
    path("candidates/", CandidateView.as_view(), name='candidates'),
    path("jobdetails/<int:pk_pass>/", JobDetails.as_view(), name='jobdetails'),
    path("jobapply/<int:jobid>/", save, name='jobapply'),
    path("candidateshow/<int:userid>/", CandidateShowView.as_view(), name = 'candidateshow' )
]