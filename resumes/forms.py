from django import forms
from .models import Resume, TechnicalSkill, SoftSkill

class ResumeForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all().order_by('name'), widget=forms.CheckboxSelectMultiple, required=True
    )

    class Meta:
        model = Resume
        fields = '__all__'