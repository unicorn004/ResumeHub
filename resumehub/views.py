from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def homepage(request):
    return render(request, 'homepage/index.html')

<<<<<<< HEAD
=======
def login_page(request):
    form = AuthenticationForm()
    return render(request, 'user_login/login.html', {'form': form})
>>>>>>> 9ed4a4f6446c35e364a37f034fa9e85afed60211
