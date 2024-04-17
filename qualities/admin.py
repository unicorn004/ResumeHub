from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('candidate','education_level','institute')

# @admin.register(Hobby)
# class HobbyAdmin(admin.ModelAdmin):
#     list_display = ('unique_id','name','slug')

# @admin.register(Skill)  # Register Skill model
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('name', 'skill_type',)
#     list_filter = ('skill_type',)
#     search_fields = ('name',)
#     prepopulated_fields = {'slug': ('name',)}

