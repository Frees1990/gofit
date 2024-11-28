from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Membership, UserMembership
from .forms import MembershipSelectForm
from .forms import MembershipForm

def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'membership/membership_list.html', {'memberships': memberships})

@login_required
def select_membership(request):
    user_membership, created = UserMembership.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = MembershipSelectForm(request.POST)
        if form.is_valid():
            selected_membership = form.cleaned_data['membership']
            user_membership.membership = selected_membership
            user_membership.save()
            return redirect('membership_confirmation')
    else:
        form = MembershipSelectForm()

    return render(request, 'membership/select_membership.html', {'form': form})

@login_required
def membership_confirmation(request):
    user_membership = UserMembership.objects.get(user=request.user)
    return render(request, 'membership/membership_confirmation.html', {
        'membership': user_membership.membership
    })

@login_required
def add_membership(request):
    """ Allow admin to add a new membership plan """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect('home')

    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membership plan added successfully!')
            return redirect('membership_list')  # Redirect to membership list page
        else:
            messages.error(request, 'Failed to add membership plan. Please ensure the form is valid.')
    else:
        form = MembershipForm()

    return render(request, 'membership/add_membership.html', {'form': form})

# View to edit an existing membership plan
@login_required
def edit_membership(request, membership_id):
    """ Allow admin to edit an existing membership plan """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect('home')

    membership = get_object_or_404(Membership, id=membership_id)

    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membership plan updated successfully!')
            return redirect('membership_list')  # Redirect to membership list page
        else:
            messages.error(request, 'Failed to update membership plan. Please ensure the form is valid.')
    else:
        form = MembershipForm(instance=membership)

    return render(request, 'membership/edit_membership.html', {'form': form, 'membership': membership})

# View to delete a membership plan
@login_required
def delete_membership(request, membership_id):
    """ Allow admin to delete a membership plan """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect('home')

    membership = get_object_or_404(Membership, id=membership_id)
    membership.delete()
    messages.success(request, 'Membership plan deleted successfully!')
    return redirect('membership_list')  # Redirect to membership list page