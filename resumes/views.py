from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resumes.models import Resume

# Create your views here.

@login_required(login_url = 'accounts:login')
def resumes(request):
    resumes = Resume.objects.filter(candidate=request.user)
    context = {
        'user':request.user,
        'resumes': resumes
    }
    return render(request, 'resumes/resumes.html', context)

@login_required(login_url = 'accounts:login')
def resume(request, slug):
    context = {
        'user': request.user,
        'slug':slug
    }
    return render(request, 'resumes/resume.html', context)
