from django import forms
from .models import Membership, UserMembership

class MembershipSelectForm(forms.Form):
    membership = forms.ModelChoiceField(
        queryset=Membership.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['name', 'description', 'price', 'duration']