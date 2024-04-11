from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage/index.html')

@login_required(login_url = 'accounts:login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def login_page(request):
    form = AuthenticationForm()
    return render(request, 'user_login/login.html', {'form': form})
