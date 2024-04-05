from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or some other page
            return redirect('qualities:home')
        else:
            # Invalid login
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user_login/login.html')

def user_logout(request):
    logout(request)
    # Redirect to a success page or some other page
    return redirect('home')

# Create your views here.
