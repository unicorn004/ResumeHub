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
    education_level_choices = [choice[1] for choice in Education.EDUCATION_LEVEL_CHOICES]

    context = {
        'form': form,
        'education_level_choices': education_level_choices,
        'user_educations': user_educations
    }
    return render(request, 'qualities/add_education.html', context)

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
