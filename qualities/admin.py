from django.contrib import admin
from .models import Education, TechnicalSkill, SoftSkill

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('candidate','education_level','institute')

@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
