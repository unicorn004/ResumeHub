from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resumes.models import Resume
from .forms import UserProfileForm
from qualities.forms import EducationForm
# Create your views here.


@login_required(login_url='accounts:login')
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qualities:add_education')  # Redirect to the dashboard after successful form submission
    else:
        form = UserProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def profile_view(request):
    return render(request, 'profile.html')

