from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import Membership
from .forms import MembershipForm

# View to display the membership list
def membership_list(request):
    memberships = Membership.objects.all()

    # Redirect to the membership detail page if the user selects a membership
    if request.method == 'POST':
        membership_id = request.POST.get('membership_pk')
        if membership_id:
            return redirect('membership_detail', membership_id=membership_id)

    return render(request, 'membership/membership_list.html', {'memberships': memberships})


def membership_detail(request, membership_id):
    membership = get_object_or_404(Membership, id=membership_id)
    return render(request, 'membership/membership_detail.html', {'membership': membership})

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
