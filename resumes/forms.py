from django import forms
from .models import Resume
from qualities.models import Skill


class ResumeForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all().order_by('name'), widget=forms.CheckboxSelectMultiple, required=True
    )

    class Meta:
        model = Resume
        fields = (
            'name',
            'description',
            'summary',
            'education',
            'skills',
            'include_address',
            'include_contact_number',
            'include_email_id',
            'target_company'
        )
