from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse_lazy


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('create_profile'))
    else:
        form = UserCreationForm()
    
    # If the form is not valid, render the same form with errors
    return render(request, 'accounts/signup.html', {'form': form})
    


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    try:
                        profile = user.profile
                        return redirect('dashboard')  # Redirect to dashboard if profile exists
                    except User.DoesNotExist:  # Handle case where User model is not found
                        pass  # Or redirect to a profile creation form here
                    except Profile.DoesNotExist:  # Catch missing profile
                        # Handle user with no profile (e.g., display a message or redirect to a profile setup page)
                        return redirect('profiles:create_profile')
            else:
                # Handle invalid login credentials (optional: add error message to context)
                pass
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})









@login_required
def dashboard_view(request):
    try:
        # Check if the user has a profile
        profile = request.user.profile
        return render(request, 'accounts/dashboard.html')
    except Profile.DoesNotExist:
        # If the user does not have a profile, redirect them to the profile creation form
        return redirect('profiles:create_profile')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
