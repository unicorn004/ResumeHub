from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resumes.models import Resume
from .forms import ResumeForm

# Create your views here.

@login_required(login_url = 'accounts:login')
def resumes(request):
    if 'create' in request.GET:
        form = ResumeForm()
        context = {
            'user': request.user,
            'form': form
        }
        return render(request, 'resumes/create_resume.html', context)
    
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.candidate = request.user
            resume.save()
            return redirect('resumes:resume', slug=resume.slug)


    resumes = Resume.objects.filter(candidate=request.user)
    context = {
        'user':request.user,
        'resumes': resumes
    }
    return render(request, 'resumes/resumes.html', context)

@login_required(login_url = 'accounts:login')
def resume(request, slug):
    resume = Resume.objects.get(slug=slug)
    print(resume.candidate)
    context = {
        'resume': resume
    }
    return render(request, 'resumes/resume.html', context)
