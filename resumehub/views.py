from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from profiles.forms import UserProfileForm

def homepage(request):
    return render(request, 'homepage/index.html')

@login_required(login_url = 'accounts:login')
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)

def login_page(request):
    form = AuthenticationForm()
    return render(request, 'user_login/login.html', {'form': form})

def profile_view(request):
    return render(request, 'profile/profile.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')


def company(request):
    return render(request, 'company/company.html', {})

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

def create_resume_view(request):
    return render(request, 'create_resume.html')