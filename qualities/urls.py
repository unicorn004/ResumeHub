from django.urls import path
from . import views

app_name = 'qualities'

urlpatterns = [
    path('', views.skills, name='home'),
    path('skills/', views.skills, name='skills'),
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:education_id>/', views.edit_education, name='edit_education'),
    path('education/delete/<int:education_id>/', views.delete_education, name='delete_education'),
]
