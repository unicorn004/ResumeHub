from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TechnicalSkill, SoftSkill
from .forms import TechnicalSkillForm, SoftSkillForm

@login_required(login_url='accounts:login')
def technical_skills(request):
    if request.method == 'POST':
        form = TechnicalSkillForm(request.POST)
        if form.is_valid():
            technical_skills = form.save(commit=False)
            technical_skills.candidate = request.user
            technical_skills.save()
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
            technical_skills = form.save(commit=False)
            technical_skills.candidate = request.user
            technical_skills.save()
            # Redirect to some view after saving the skill
            return redirect('soft_skills')
    else:
        form = SoftSkillForm()
    
    context = {
        'user': request.user,
        'form': form
    }
    return render(request, 'resumes/soft_skills.html', context)



from .forms import EducationForm
from .models import Education
from django.forms.models import model_to_dict


@login_required(login_url='accounts:login')
def add_education(request):
    user_education, created = Education.objects.get_or_create(candidate=request.user)

    if request.method == 'POST':
      form = EducationForm(request.POST, instance=user_education)
      if form.is_valid():
           form.save()  # Save the form data to the database
           return redirect('dashboard')  # Redirect back to the dashboard after saving

    else:
        # No POST data, instantiate the form with the existing or newly created instance
        form = EducationForm(instance=user_education)

    context = {
        'form': form,
    }
    return render(request, 'qualities/add_education.html', context)


# views.py in the qualities app

from django.shortcuts import get_object_or_404
@login_required(login_url='accounts:login')
def edit_education(request, education_id):
    education_entry = get_object_or_404(Education, id=education_id, candidate=request.user)
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
    return render(request, 'qualities/edit_education.html', context)

def delete_education(request, education_id):
    education_entry = get_object_or_404(Education, id=education_id)
    education_entry.delete()
    return redirect('qualities:add_education')
