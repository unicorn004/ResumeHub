from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Profile

class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', max_length=100)
    address = forms.CharField(label='Address', widget=forms.Textarea)
    age = forms.IntegerField(label='Age', validators=[MinValueValidator(0), MaxValueValidator(150)])
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email Address')

    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'age', 'phone_number', 'email']  # Rearrange fields
