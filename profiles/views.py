from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resumes.models import Resume
from .forms import UserProfileForm
from qualities.forms import EducationForm
# Create your views here.



def profile_view(request):
    return render(request, 'profile.html')

