from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = 'accounts:login')
def resumes(request):
    return render(request, 'resumes/resumes.html')

@login_required(login_url = 'accounts:login')
def resume(request, slug):
    context = {
        'user': request.user,
        'slug':slug
    }
    return render(request, 'resumes/resume.html', context)
