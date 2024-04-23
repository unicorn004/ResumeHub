from django.urls import path
from . import views

app_name = 'qualities'

urlpatterns = [
    path('', views.skills, name='home'),
    path('skills/', views.skills, name='skills'),
]