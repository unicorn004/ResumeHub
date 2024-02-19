from django.contrib import admin
from .models import Hobby, Testimonial, WorkExperience, Resume

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'unique_id')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('source', 'content', 'date', 'unique_id')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'location', 'employment_duration', 'unique_id' ,'responsibilities')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('unique_id','personal_information','education','skills','work_experience','achievements','projects','additional_sections')
