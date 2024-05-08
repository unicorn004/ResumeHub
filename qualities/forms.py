from django import forms
from .models import TechnicalSkill, SoftSkill, Education

class TechnicalSkillForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows': 4}))
    
    programming_language = 'programming_language'
    frameworks = 'frameworks'
    version_control = 'version_control'
    methodologies = 'methodologies'
    data_analysis = 'data_analysis'
    it_networking = 'it_networking'
    web_dev_design = 'web_dev_design'
    ai_ml = 'ai_ml'
    dbms = 'dbms'
    cloud_computing = 'cloud_computing'
    devops = 'devops'
    other = 'other'
    
    CATEGORY_CHOICES = [
        (programming_language, 'Programming Language'),
        (frameworks, 'Frameworks and Libraries'),
        (version_control, 'Version Control Systems'),
        (methodologies, 'Development Methodologies'),
        (data_analysis, 'Data Analysis and Analytics'),
        (it_networking, 'IT and Networking'),
        (web_dev_design, 'Web Development and Design'),
        (ai_ml, 'Machine Learning and Artificial Intelligence'),
        (dbms, 'Database Management'),
        (cloud_computing, 'Cloud Computing'),
        (devops, 'DevOps'),
        (other, 'Other')
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = TechnicalSkill
        exclude = ['unique_id']  # Exclude the unique_id field

class SoftSkillForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows': 4}))
    category = forms.CharField(label='Category', max_length=25)
    
    team_management = 'team_management'
    communication = 'communication'
    leadership = 'leadership'
    problem_solving = 'problem_solving'
    adaptability = 'adaptability'
    time_management = 'time_management'
    conflict_resolution = 'conflict_resolution'
    teamwork = 'teamwork'
    negotiation = 'negotiation'
    creativity = 'creativity'
    decision_making = 'decision_making'
    mentoring = 'mentoring'
    stress_management = 'stress_management'

    CATEGORY_CHOICES = [
        (team_management, 'Team Management'),
        (communication, 'Communication'),
        (leadership, 'Leadership'),
        (problem_solving, 'Problem Solving'),
        (adaptability, 'Adaptability'),
        (time_management, 'Time Management'),
        (conflict_resolution, 'Conflict Resolution'),
        (teamwork, 'Teamwork'),
        (negotiation, 'Negotiation'),
        (creativity, 'Creativity'),
        (decision_making, 'Decision Making'),
        (mentoring, 'Mentoring'),
        (stress_management, 'Stress Management')
    ]
    
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = SoftSkill
        exclude = ['unique_id']  # Exclude the unique_id field

#class EducationForm(forms.ModelForm):
    #class Meta:
        #model = Education
        #fields = ['education_level', 'institute', 'additional_info', 'date_of_passing', 'pursuing']

class EducationForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', max_length=100)
    education_level = forms.ChoiceField(label='Education Level', choices=Education.EDUCATION_LEVEL_CHOICES)
    date_of_passing = forms.DateField(label='Date of Passing', widget=forms.TextInput(attrs={'class': 'datepicker'}))
    additional_info = forms.CharField(label='Additional Info', widget=forms.Textarea)
    pursuing = forms.BooleanField(label='Pursuing', required=False)  # Add this line
    

    class Meta:
        model = Education
        fields = ['full_name', 'institute', 'date_of_passing', 'additional_info', 'pursuing']  # Include the pursuing field
