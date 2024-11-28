from django import forms
from .models import Membership
from django.contrib.auth.models import User


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['name', 'description', 'price'] 
