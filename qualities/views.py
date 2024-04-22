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
