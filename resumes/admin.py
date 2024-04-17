from django.contrib import admin
from .models import Resume
from qualities.models import Education

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "education":
    #         kwargs["queryset"] = Education.objects.filter(candidate=request.user, institute='Sardar Patel Institute of Technology')
    #     return super(ResumeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    list_display = ('candidate', 'name', 'description',)