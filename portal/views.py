# portal/views.py
from candidates.models import Candidate
from django.contrib.auth import models
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.base import TemplateView, View
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User
from django.contrib.auth import login, authenticate
from candidates.models import Candidate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
import social_django


class Dashboard(generic.ListView):
    template_name= "portal/dashboard.html"
    model = Candidate

    # Checking is user candidate by geting the Candidate model objects
    def get(self, request):
        # import pdb
        # pdb.set_trace()
        iscandidate = False
        if request.user.is_authenticated:
            if request.user.social_auth.filter(provider="google-oauth2"):
                return render(request, self.template_name)
            elif request.user.groups.all()[0].name == 'Candidates' :
                if Candidate.objects.filter(c_username= request.user):
                    # cuser= Candidate.objects.get(c_username= request.user)
                    iscandidate = True
                    args = {'iscandidate': iscandidate}
                    return render(request, self.template_name, args)
                else:
                    addcandidate = True
                    args = {'addcandidate': addcandidate}
                    return render(request, self.template_name, args)
            else:
                return render(request, self.template_name)

        else:
            return render(request, self.template_name)


#Sign Up View creating from register form
class SignupView(generic.CreateView):
    template_name = 'portal/signup.html'
    success_url = reverse_lazy("dashboard")
    form_class = CustomUserCreationForm

    #Moving user to admin group while signing up using uertype field
    def post(self, request, *args, **kwargs):
        pass
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usertype = form.cleaned_data['usertype']
            if usertype == 'candidate':
                user = form.save(commit=False)
                user.save()
                user_group = Group.objects.get(name='Candidates')
                user.groups.add(user_group)
                return redirect('login')
            else:
                user = form.save(commit=False)
                user.save()
                user_group = Group.objects.get(name='Clients')
                user.groups.add(user_group)
                return redirect('login')
        else:
            return render(request, self.template_name, {'form' : form })


def send_email(request):
    # subject = request.POST.get('subject', '')
    # message = request.POST.get('message', '')
    # from_email = request.POST.get('from_email', '')
    # subject = 'Subject'
    # message = 'Message'
    # from_email = ['sanscodex@gmail.com']
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['isanooptp@gmail.com'])
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect('/dashboard')
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are e ntered and valid.')
    

    email = EmailMessage('Subject', 'Body', to=['isanooptp@gmail.com'])
    email.send()
    return HttpResponseRedirect('')

