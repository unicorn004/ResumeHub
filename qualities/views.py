from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from qualities.models import Skill
from .forms import SkillForm

@login_required(login_url='accounts:login')
def skills(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save()
            # Redirect to some view after saving the skill
            return redirect(request, 'resumes/skills.html', context)
    else:
        form = SkillForm()
    
    context = {
        'user': request.user,
        'form': form
    }
    return render(request, 'resumes/skills.html', context)


# views.py in qualities app
from .forms import EducationForm
from .models import Education
@login_required(login_url='accounts:login')
def add_education(request):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        form.instance.candidate = request.user
        form.save()
        return redirect('resumes:resumes')
    
    educations = Education.objects.filter(candidate=request.user)
    context = {
        'user': request.user,
        'form': form,
        'educations': educations
    }
    return render(request, 'qualities/add_education.html', context)
