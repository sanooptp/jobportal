from django.conf.urls import url
from django.urls import path,include
from .views import ClientDashboardView, JobAppliedView, JobList, JobCancelView, JobView, AppliedCandidatesView, jobaccept, jobreject
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("jobform/", JobView.as_view(), name='jobform'),
    path("joblist/", JobList.as_view(), name='joblist'),
    path('clientdashboard/', ClientDashboardView.as_view(), name='clientdashboard'),
    path('jobapplied/',JobAppliedView.as_view(),name='jobapplied'),
    path('jobapplied/<int:jobid>',JobAppliedView.as_view(),name='jobapplied'), 
    path('jobcancel/<int:job>',  JobCancelView.as_view(), name= 'jobcancel'),
    path('candidatesapplied/<int:jobid>', AppliedCandidatesView.as_view(), name = 'candidatesapplied'),
    path('jobaccept/<int:jobid>',jobaccept, name = 'jobaccept'),
    path('jobreject/<int:jobid>',jobreject, name = 'jobreject'),
    path('joblist/<str:search>', JobList.as_view(),name= 'jobsearch')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
