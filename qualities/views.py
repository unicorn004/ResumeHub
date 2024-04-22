from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SkillForm
from resumes.models import Resume
from resumes.forms import ResumeForm


def home(request):
    return render(request, 'homepage/index.html')
  # Assuming 'index.html' is your homepage template
  

@login_required(login_url='accounts:login')
def add_skill(request, resume_slug):
    resume = Resume.objects.get(slug=resume_slug)

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.resume = resume
            skill.save()
            return redirect('resumes:resume', slug=resume.slug)

    else:
        form = SkillForm()

    context = {
        'resume': resume,
        'form': form
    }
    return render(request, 'resumes/add_skill.html', context)


