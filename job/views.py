from django.shortcuts import render , redirect
from .models import Job
from django.core.paginator import Paginator
from.forms import Applyform , Jobform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .fillters import JobFilter


# Create your views here.

def job_list(request):
    job_list= Job.objects.all()

    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={'job_list':page_obj,'T':job_list,'myfilter':myfilter}
    return render(request,'job/jobs.html',context)


def job_details(request,slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = Applyform(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form= Applyform()

    context={'job':job_detail,'form':form}

    return render(request,'job/job_details.html',context)

@login_required
def add_job(request):
    
    if request.method == 'POST':
        form=Jobform(request.POST , request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:jobs'))
    else:
        form=Jobform()

    return render(request,'job/add_job.html',{'form':form})