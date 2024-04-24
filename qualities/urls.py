from django.urls import path
from . import views

app_name = 'qualities'

urlpatterns = [
    path('technical_skills/', views.technical_skills, name='technical_skills'),  # Route to view for technical skills
    path('soft_skills/', views.soft_skills, name='soft_skills'),  # Route to view for soft skills
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:education_id>/', views.edit_education, name='edit_education'),
    path('education/delete/<int:education_id>/', views.delete_education, name='delete_education'),
]

