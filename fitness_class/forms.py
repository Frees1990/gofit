from django import forms
from .models import FitnessClass

class FitnessClassForm(forms.ModelForm):
    class Meta:
        model = FitnessClass
        fields = ['name', 'day', 'start_time', 'end_time']
