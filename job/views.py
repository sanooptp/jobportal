from django.contrib.auth import models
from candidates.models import Candidate
from django.shortcuts import get_object_or_404, render
from .forms import JobForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Job, JobApplied
from django.contrib.auth.models import User
from candidates.models import Candidate
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# job adding form
class JobView(generic.CreateView):
    template_name = 'job/jobform.html'
    form_class = JobForm
    success_url = reverse_lazy("clientdashboard")
    def post(self, request):
        # import pdb
        # pdb.set_trace()
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES or None)
            if form.is_valid():
                fs = form.save(commit = False)
                fs.creator =request.user
                form.save()
                return redirect('clientdashboard')
        else:
            form = JobForm()
        return render(request, self.template_name, {'form': form})

# displaying the job details from job model     
class  JobList(generic.ListView):
    template_name = 'job/joblist.html'  
    model =Job
    def get(self, request):
        if request.method == "GET":
            item = request.GET.get('search')
            if item:
                jobs= Job.objects.filter(job_name__contains = item)
            else:
                jobs = Job.objects.all()
        args = { 'jobs': jobs}
        return render(request, self.template_name, args)

class ClientDashboardView(generic.ListView):
    template_name = 'job/clientdashboard.html'
    model = Job
    def get(self, request):
        jobs = Job.objects.filter(creator = request.user)       
        args = { 'jobs': jobs}
        if request.user.groups.all()[0].name == 'Clients' :
            return render(request, self.template_name, args)
        else:
            return redirect('joblist')

class JobAppliedView(generic.ListView):
    template_name = 'job/jobapplied.html'
    model = JobApplied

    def get(self, request):
        # import pdb
        # pdb.set_trace()
        jobapply = JobApplied.objects.all()
        args = { 'jobs': jobapply}
        return render(request, self.template_name, args)
    
class JobCancelView(generic.CreateView):
    model = JobApplied
    def get(self, request, job):
        self.model.objects.filter(id=job).delete()
        return redirect('jobapplied')

class AppliedCandidatesView(generic.CreateView):
    template_name = 'job/appliedcandidates.html'
    model = JobApplied
    
    def get(self, request, jobid):
        current_job = Job.objects.get(id = jobid)
        candidate = Candidate.objects.all()
        jobs = self.model.objects.filter(job_applied = current_job)
        args = { 'jobs': jobs, 'current_job': current_job, 'candidate' : candidate}
        return render(request, self.template_name, args)

def jobaccept(request, jobid):
    update = JobApplied.objects.filter(id= jobid).update(status= 'Accepted')
    return redirect('clientdashboard')

def jobreject(request, jobid):
    update = JobApplied.objects.filter(id= jobid).update(status= 'Rejected')
    return redirect('clientdashboard')