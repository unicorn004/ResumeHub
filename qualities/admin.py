from django.contrib import admin
from .models import Hobby

# Register your models here.
@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)

