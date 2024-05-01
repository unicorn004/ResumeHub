from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name','contact_number', 'address', 'birth_date', 'linkedin_url', 'instagram_url', 'facebook_url')
    search_fields = ('user__username', 'contact_number', 'address', 'linkedin_url', 'instagram_url', 'facebook_url')
