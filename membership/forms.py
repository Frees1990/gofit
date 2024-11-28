from django import forms
from .models import UserMembership
from django.contrib.auth.models import User

class MembershipSignUpForm(forms.ModelForm):
    # Additional fields for the user's personal details
    first_name = forms.CharField(max_length=100, required=True, label='First Name')
    last_name = forms.CharField(max_length=100, required=True, label='Last Name')
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True, label='Address')
    phone_number = forms.CharField(max_length=15, required=True, label='Phone Number')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = UserMembership
        fields = ['membership']  # The form will still include the membership field
        # You can add other fields if you want to save them in UserMembership or elsewhere

    def save(self, commit=True):
        # First, save the User model if it's necessary to update or create a new user
        user = super().save(commit=False)
        # Here you would save the User details
        if commit:
            user.save()
        return user
