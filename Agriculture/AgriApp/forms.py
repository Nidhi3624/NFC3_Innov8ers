# forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,  # or any other max length you prefer
        required=True,
        help_text='',  # This will remove the default help text
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'})  # Optional: Add placeholder
    )
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15)
    country = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'phone', 'country', 'state', 'city', 'address', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match")

        return cleaned_data
