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
