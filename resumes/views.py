from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from resumes.models import Resume
from .forms import ResumeForm
from profiles.models import Profile

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

def resume(request, slug):
    # Assuming 'slug' is used to identify the user whose profile to display
    resume = get_object_or_404(Resume, slug=slug) # Fetch the profile based on the user's username
    
    context = {
        'resume': resume,
    }
    return render(request, 'resumes/resume.html', context)
