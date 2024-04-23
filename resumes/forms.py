from django import forms
from .models import Resume, TechnicalSkill, SoftSkill

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        exclude = ['unique_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['technical_skills'] = forms.ModelMultipleChoiceField(
            queryset=TechnicalSkill.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
        self.fields['soft_skills'] = forms.ModelMultipleChoiceField(
            queryset=SoftSkill.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
