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

    return render(request, 'resumes/skills.html', context)
# views.py in the qualities app

from .forms import EducationForm
from .models import Education
@login_required(login_url='accounts:login')
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.candidate = request.user
            education.save()
            return redirect('qualities:add_education')  # Redirect back to the same page
    else:
        form = EducationForm()

    # Fetch the user's education entries
    user_educations = Education.objects.filter(candidate=request.user)

    return render(request, 'qualities/add_education.html', {'form': form, 'user_educations': user_educations})


# views.py in the qualities app

from django.shortcuts import get_object_or_404

def edit_education(request, education_id):
    education_entry = get_object_or_404(Education, id=education_id)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education_entry)
        if form.is_valid():
            form.save()
            return redirect('qualities:add_education')  # Redirect to the add education page
    else:
        form = EducationForm(instance=education_entry)
    
    context = {
        'form': form,
    }
    return render(request, 'edit_education.html', context)

def delete_education(request, education_id):
    education_entry = get_object_or_404(Education, id=education_id)
    education_entry.delete()
    return redirect('qualities:add_education')
