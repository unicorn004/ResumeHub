from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resumes.models import Resume
from .forms import UserProfileForm
from qualities.forms import EducationForm
from .models import Profile

#@login_required(login_url='accounts:login')
def create_profile(request):
    try:
        # Retrieve the user's profile if it exists
        profile_instance = Profile.objects.get(user=request.user)
        
        if request.method == 'POST':
            # If the form is submitted with POST data, process the data
            form = UserProfileForm(request.POST, instance=profile_instance)
            if form.is_valid():
                # If the form data is valid, save the form
                form.save()
                return redirect('qualities:add_education')
            else:
                # Form is invalid, log errors
                print(form.errors)
        else:
            # If the request is a GET request (i.e., initial page load), populate the form with existing data
            form = UserProfileForm(instance=profile_instance)
    except Profile.DoesNotExist:
        # If the user does not have a profile yet, create a new profile
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('qualities:add_education')
        else:
            form = UserProfileForm()

    return render(request, 'create_profile.html', {'form': form})



def profile_view(request):
    return render(request, 'profile.html')

