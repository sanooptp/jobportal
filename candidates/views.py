from django.db import models
from django.shortcuts import render, get_object_or_404
from .forms import CandidateForm, JobApplyForm
from django.views import generic
from django.urls import reverse_lazy
from job.models import Job,JobApplied
from django.contrib.auth.models import User
from .models import Candidate
from django.http import HttpResponse, request,HttpResponseRedirect
from django.shortcuts import redirect


class CandidateView(generic.CreateView):
    template_name = 'candidates/candidate.html'
    form_class = CandidateForm
    success_url = reverse_lazy("joblist")
    
    def get(self, request):
        form= self.form_class()
        if request.user.is_authenticated:
            if Candidate.objects.filter(c_username = request.user):
                item = Candidate.objects.get(c_username = request.user)
                initial_data={            
                'name':item.name,
                'age': item.age,
                'gender': item.gender,
                'mobile':item.mobile,
                'city': item.city,
                'exp_salary': item.exp_salary,
                'relocate': item.relocate,
                'resume': item.resume
                }
                
                form= self.form_class(initial= initial_data)
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('login')
        
    def post(self, request):
        # import pdb
        # pdb.set_trace()
        if request.method == 'POST':
            if Candidate.objects.filter(c_username = request.user):
                item = Candidate.objects.get(c_username = request.user)
                form = self.form_class(request.POST, request.FILES, instance= item)
            else:
                form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                fs = form.save(commit = False)
                fs.c_username =request.user
                form.save()
                return redirect('joblist')
        else:
            form = CandidateForm()
        return render(request, self.template_name, {'form': form})


class  JobDetails(generic.CreateView):
    template_name = 'candidates/jobdetails.html'
    form_class = JobApplyForm
    
    # def formvalid(self, request, jobid):
    #     if request.method == "POST":
    #         candidate = self.form_class.save(commit=False)
    #         candidate.username = request.user  
    #         candidate.candidate = Candidate.objects.get(c_username = request.user)
    #         candidate.status= 'Pending'
    #         candidate.job_applied = Job.objects.get(id=jobid)
    #         candidate.save()

    def get(self, request,pk_pass):
        jobs = Job.objects.get(id=pk_pass)
        # if JobApplied.objects.get(username= request.user):
            # candidate= JobApplied.objects.get(username= request.user).status
        args = { 'jobs': jobs}
        return render(request, self.template_name, args)

def save(request,jobid):
    candidate = User
    jobapplied = Job.objects.get(id=jobid)
    status= 'Pending'
    apply = JobApplied(username= request.user, job_applied = jobapplied, status= status)
    apply.save()
    return HttpResponseRedirect('/joblist')


class CandidateShowView(generic.CreateView):
    template_name = 'candidates/candidateshow.html'
    model = Candidate
    def get(self,request, userid):
        candidate = self.model.objects.get(c_username = userid)
        args = {'candidate': candidate}
        return render(request, self.template_name, args)  
# jkldsjflk