from django import forms
from .models import Membership, UserMembership

class MembershipSelectForm(forms.Form):
    membership = forms.ModelChoiceField(
        queryset=Membership.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )
