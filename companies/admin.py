from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # list_display = ('image_tag', 'name', 'email', 'created_at', 'published')
    list_display = ('name', 'description', 'email',)

    # def image_tag(self, obj):
    #     return format_html(f'<img src="{obj.logo.url}" style="height:10vh; border-radius: 5%;" />')
