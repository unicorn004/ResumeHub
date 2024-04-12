from django.urls import path, include
from . import views

app_name = 'resumes'

urlpatterns= [

    # All resumes
    path('', views.resumes, name='resumes'),

    # Individual resume
    path('<slug>', views.resume, name='resume'),

]
