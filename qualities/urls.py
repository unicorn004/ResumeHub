from django.urls import path
from . import views

app_name = 'qualities'

urlpatterns = [
    path('', views.skills, name='home'),
    path('skills/', views.skills, name='skills'),
]


urlpatterns = [
    path('add_education/', views.add_education, name='add_education'),
]
