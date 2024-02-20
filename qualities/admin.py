from django.contrib import admin
from .models import Hobby, Skill  # Import Skill model

# Register your models here.
@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('unique_id','name','slug')

@admin.register(Skill)  # Register Skill model
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type',)
    list_filter = ('skill_type',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
