from django import forms
from .models import TechnicalSkill, SoftSkill, Education

class TechnicalSkillForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows': 4}))
    category = forms.CharField(label='Category', max_length=25)

    class Meta:
        model = TechnicalSkill
        exclude = ['unique_id']  # Exclude the unique_id field

class SoftSkillForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows': 4}))
    category = forms.CharField(label='Category', max_length=25)

    class Meta:
        model = SoftSkill
        exclude = ['unique_id']  # Exclude the unique_id field

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['education_level', 'institute', 'additional_info', 'date_of_passing', 'pursuing']
