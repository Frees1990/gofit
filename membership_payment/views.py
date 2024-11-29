from django.shortcuts import render
from .forms import MembershipPaymentForm

def payment_view(request):
    if request.method == "POST":
        form = MembershipPaymentForm(request.POST)
        if form.is_valid():
            # You can proceed with Stripe payment processing here
            stripe_token = form.cleaned_data['stripe_token']
            print("Stripe token received:", stripe_token)

            # Your Stripe charge creation code goes here (e.g., stripe.Charge.create(...))

            return render(request, 'membership_payment/success.html')  # Redirect to success page after payment
        else:
            # Handle form errors
            print("Form errors:", form.errors)

    else:
        form = MembershipPaymentForm()

    return render(request, 'membership_payment/payment_form.html', {'form': form})


def success_view(request):
    # Example subscription data
    subscription = {
        "plan_name": "Premium Membership",
        "start_date": "2024-11-29",
        "email": "user@example.com",
    }

    print("Subscription data being passed:", subscription)
     
    return render(request, "success.html", {"subscription": subscription})

