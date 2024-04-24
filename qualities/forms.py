from django import forms
from .models import Skill
from .models import Education

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

        # forms.py in qualities app


#class EducationForm(forms.ModelForm):
    #class Meta:
        #model = Education
        #fields = ['education_level', 'institute', 'additional_info', 'date_of_passing', 'pursuing']
from django import forms
from .models import Education

class EducationForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', max_length=100)
    education_level = forms.ChoiceField(label='Education Level', choices=Education.EDUCATION_LEVEL_CHOICES)
    date_of_passing = forms.DateField(label='Date of Passing', widget=forms.TextInput(attrs={'class': 'datepicker'}))
    additional_info = forms.CharField(label='Additional Info', widget=forms.Textarea)
    pursuing = forms.BooleanField(label='Pursuing', required=False)  # Add this line
    


    class Meta:
        model = Education
        fields = ['full_name', 'institute', 'date_of_passing', 'additional_info', 'pursuing']  # Include the pursuing field
