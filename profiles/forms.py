from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .fields import PhoneNumberField
from .models import Profile

class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', max_length=100)
    address = forms.CharField(label='Address', widget=forms.Textarea)
    birth_date = forms.TimeField(label='BirthDate')
    phone_number = forms.CharField(label='Contact Number')
    bio = forms.CharField(label='Bio', max_length=500)
    email = forms.EmailField(label='Email Address')
    linkedin_url = forms.URLField(label='LinkedIn URL', max_length=200, required=False)
    instagram_url = forms.URLField(label='Instagram URL', max_length=200, required=False)
    facebook_url = forms.URLField(label='Facebook URL', max_length=200, required=False)

    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'birth_date', 'phone_number','bio', 'email', 'linkedin_url', 'instagram_url', 'facebook_url']
