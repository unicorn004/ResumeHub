from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def homepage(request):
    return render(request, 'homepage/index.html')

def login_page(request):
    form = AuthenticationForm()
    return render(request, 'user_login/login.html', {'form': form})