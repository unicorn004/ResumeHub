from django import forms
from .models import Resume, TechnicalSkill, SoftSkill , Company

class ResumeForm(forms.ModelForm):
    technical_skills = forms.ModelMultipleChoiceField(
        queryset=TechnicalSkill.objects.all().order_by('category'),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Set to True if technical skills are mandatory
    )

    soft_skills = forms.ModelMultipleChoiceField(
        queryset=SoftSkill.objects.all().order_by('category'),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Set to True if soft skills are mandatory
    )
    
    target_company = forms.ModelMultipleChoiceField(
        queryset=Company.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Set to True if soft skills are mandatory
    )

    class Meta:
        model = Resume
        fields = ['name','description','summary','target_company','technical_skills','soft_skills']
