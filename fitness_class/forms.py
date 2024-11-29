from django import forms
from .models import Booking
from .models import FitnessClass

class FitnessClassForm(forms.ModelForm):
    class Meta:
        model = FitnessClass
        fields = ['name', 'day', 'start_time', 'end_time']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fitness_class']

    # You can customize widgets here if you want to style them differently
    fitness_class = forms.ModelChoiceField(queryset=FitnessClass.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))