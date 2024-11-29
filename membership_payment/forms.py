# membership_payment/forms.py

from django import forms
from membership.models import Membership  # Import your Membership model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MembershipPaymentForm(forms.Form):
    # Add personal details fields
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    # Add billing address and mobile number fields
    billing_address = forms.CharField(max_length=255, required=True, label="Billing Address")
    mobile_number = forms.CharField(max_length=15, required=True, label="Mobile Number")
    
    # Select membership plan
    membership = forms.ModelChoiceField(queryset=Membership.objects.all(), empty_label="Choose a Plan")
    
    # Stripe token will be added after collecting card details
    stripe_token = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Subscribe'))
