from django.urls import path, include
from .views import create_profile
from .views import profile_view
from . import views

app_name = 'profiles'

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    # Other URL patterns for your project...

    path('profile.html', views.profile_view, name='profile_html'),
]
