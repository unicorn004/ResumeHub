from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TechnicalSkill, SoftSkill
from .forms import TechnicalSkillForm, SoftSkillForm

@login_required(login_url='accounts:login')
def technical_skills(request):
    if request.method == 'POST':
        form = TechnicalSkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.candidate = request.user
            skill.save()
            # Redirect to some view after saving the skill
            return redirect('technical_skills')
    else:
        form = TechnicalSkillForm()
    
    context = {
        'user': request.user,
        'form': form
    }
    return render(request, 'resumes/technical_skills.html', context)

@login_required(login_url='accounts:login')
def soft_skills(request):
    if request.method == 'POST':
        form = SoftSkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.candidate = request.user
            skill.save()
            # Redirect to some view after saving the skill
            return redirect('soft_skills')
    else:
        form = SoftSkillForm()
    
    context = {
        'user': request.user,
        'form': form
    }
    return render(request, 'resumes/soft_skills.html', context)



# views.py in qualities app
from .forms import EducationForm
from .models import Education
@login_required(login_url='accounts:login')
def add_education(request):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        form.instance.candidate = request.user
        form.save()
        return redirect('add_education')
    
    educations = Education.objects.filter(candidate=request.user)
    context = {
        'user': request.user,
        'form': form,
        'educations': educations
    }
    return render(request, 'qualities/add_education.html', context)
