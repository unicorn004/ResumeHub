# urls.py
from django.urls import path
from . import views

app_name = 'qualities'

urlpatterns = [
    path('resumes/', views.add_skill , name='resumes'),
    path('resume/<slug:slug>/', views.add_skill , name='resume'),
    path('resume/<slug:resume_slug>/add-skill/', views.add_skill, name='add_skill'),
]
