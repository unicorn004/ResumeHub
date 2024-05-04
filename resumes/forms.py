from django import forms
from .models import Resume, Company
from qualities.models import TechnicalSkill,SoftSkill

class ResumeForm(forms.ModelForm):
    technical_skills = forms.ModelChoiceField(
        queryset=TechnicalSkill.objects.all().order_by('category'),
        widget=forms.Select,
        required=False,  # Set to True if technical skills are mandatory
        empty_label="Enter your technical skill"
    )

    soft_skills = forms.ModelChoiceField(
        queryset=SoftSkill.objects.all().order_by('category'),
        widget=forms.Select,
        required=False,  # Set to True if soft skills are mandatory
        empty_label="Enter your soft skill"
    )
    
    target_company = forms.ModelChoiceField(
        queryset=Company.objects.all().order_by('name'),
        widget=forms.Select,
        required=False,  # Set to True if target companies are 
        empty_label="Enter your target company here"
    )


    class Meta:
        model = Resume
        fields = ['name','description','summary','target_company','technical_skills','soft_skills']
