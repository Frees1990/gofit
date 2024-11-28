from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import Membership, UserMembership
from .forms import MembershipSignUpForm

# View to display the membership list
def membership_list(request):
    memberships = Membership.objects.all()

    # Redirect to the membership detail page if the user selects a membership
    if request.method == 'POST':
        membership_id = request.POST.get('membership_id')
        if membership_id:
            return redirect('membership_detail', membership_id=membership_id)

    return render(request, 'membership/membership_list.html', {'memberships': memberships})

def membership_detail(request, membership_id):
    # Get the selected membership or return a 404 if not found
    membership = get_object_or_404(Membership, id=membership_id)

    # Handle the sign-up process
    if request.method == 'POST':
        form = MembershipSignUpForm(request.POST)
        if form.is_valid():
            # Save the user membership (add membership to the user)
            user_membership = form.save(commit=False)
            user_membership.user = request.user
            user_membership.membership = membership
            user_membership.save()

            messages.success(request, 'You have successfully signed up for the membership!')
            return redirect('membership_confirmation')  # Redirect to a confirmation page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MembershipSignUpForm()

    return render(request, 'membership/membership_detail.html', {
        'membership': membership,
        'form': form
    })

# View to display user's membership confirmation
@login_required
def membership_confirmation(request):
    try:
        # Check if the user has a membership
        user_membership = UserMembership.objects.get(user=request.user)
    except UserMembership.DoesNotExist:
        # If the user does not have a membership, show an error message
        messages.error(request, 'You have not signed up for a membership yet.')
        return redirect('membership_list')  # Redirect back to the membership list

    # Redirect to the profile page after successful membership sign-up
    return redirect('profile') 

# Admin Views to manage memberships (unchanged)
@login_required
def add_membership(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect('home')

    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membership plan added successfully!')
            return redirect('membership_list')
        else:
            messages.error(request, 'Failed to add membership plan. Please ensure the form is valid.')
    else:
        form = MembershipForm()

    return render(request, 'membership/add_membership.html', {'form': form})

@login_required
def edit_membership(request, membership_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect('home')

    membership = get_object_or_404(Membership, id=membership_id)

    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membership plan updated successfully!')
            return redirect('membership_list')
        else:
            messages.error(request, 'Failed to update membership plan. Please ensure the form is valid.')
    else:
        form = MembershipForm(instance=membership)

    return render(request, 'membership/edit_membership.html', {'form': form, 'membership': membership})

@login_required
def delete_membership(request, membership_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect('home')

    membership = get_object_or_404(Membership, id=membership_id)
    membership.delete()
    messages.success(request, 'Membership plan deleted successfully!')
    return redirect('membership_list')
