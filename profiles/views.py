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
            email = request.POST.get('email')
            if email:
                request.user.email = email
                request.user.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been updated successfully!")
            return redirect('profile')

    else:
        form = UserProfileForm(instance=profile)
        password_form = PasswordChangeForm(request.user)

    # ✅ Corrected order query
    orders = Order.objects.filter(user_profile=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'password_form': password_form,
    }

    return render(request, template, context)
