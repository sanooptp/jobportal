from django.conf.urls import url, include
from django.urls import path
from . import views
from .views import SignupView, Dashboard, send_email
from candidates.views import CandidateView

urlpatterns = [
    path('',Dashboard.as_view(),name='dashboard'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('candidates/', CandidateView.as_view(),name='candidates'),
    path('sendemail', send_email ,name= 'sendemail'),
]
    