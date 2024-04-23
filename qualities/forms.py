from django import forms
from .models import Skill
from .models import Education

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

        # forms.py in qualities app


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['education_level', 'institute', 'additional_info', 'date_of_passing', 'pursuing']
