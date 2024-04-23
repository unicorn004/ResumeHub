from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resumes.models import Resume
from .forms import UserProfileForm

# Create your views here.


@login_required(login_url = 'accounts:login')
def create_profile(request):
    if 'createp' in request.GET:
        form = UserProfileForm()
        context = {
            'user': request.user,
            'form': form
        }
        return render(request, 'create_profile.html', context)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.save()
            return redirect('dashboard', slug=resume.slug)


    resumes = Resume.objects.filter(candidate=request.user)
    context = {
        'user':request.user,
        'resumes': resumes
    }
    return render(request, 'resumes/resumes.html', context)
