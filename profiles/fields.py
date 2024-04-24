# Inside your_app/fields.py

from django import forms

class PhoneNumberField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)  # Set max length to 10
        super().__init__(*args, **kwargs)

    def clean(self, value):
        value = super().clean(value)
        if not value.isdigit() or len(value) != 10:
            raise forms.ValidationError('Please enter a valid 10-digit phone number.')
        return value
