"""
URL configuration for resumehub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

# Customise admin headings
admin.site.site_header = "ResumeHub Admin"
admin.site.site_title = "ResumeHub Admin Portal"
admin.site.index_title = "Welcome to ResumeHub Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', include('companies.urls', namespace='companies')),
    path('', views.homepage, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
   
    # Resume specific paths
    path('resumes/', include('resumes.urls')),

    # Account specific paths
    path('accounts/', include('accounts.urls')),
    
    path('qualities/', include('qualities.urls', namespace='qualities')),

    path('profiles/', include('profiles.urls')),
    path('technical_skills/',include('qualities.urls', namespace='technical_skills')),
    
    path('soft_skills/',include('qualities.urls', namespace='soft_skills')),

    path('profile/', views.profile_view, name='profile'),

    path('signup/', views.signup_view, name='signup'),

    path('create_profile/', views.create_profile, name='create_profile'),

    path('company/', views.company, name='company'),
    
    path('create_resume/', views.create_resume_view, name='resume_form'),


    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),

    path('aboutus.html', views.aboutus, name='aboutus'),
    path('dashboard/company/', views.company, name='company'),
     path('faq.html', views.faq, name='faq'),
    

]