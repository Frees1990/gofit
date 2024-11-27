from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Membership, UserMembership
from .forms import MembershipSelectForm

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