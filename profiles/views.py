from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile and allow updates """
    profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        password_form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            request.user.email = request.POST.get('email')  # Save updated email
            request.user.save()
            messages.success(request, "Profile updated successfully!")
        else:
            messages.error(request, "Failed to update profile. Please ensure the form is valid.")

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Prevents logout after password change
            messages.success(request, "Your password has been updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Failed to update password. Please check the form.")

    else:
        form = UserProfileForm(instance=profile)
        password_form = PasswordChangeForm(request.user)

    # Get user's order history
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'password_form': password_form,
    }

    return render(request, template, context)
