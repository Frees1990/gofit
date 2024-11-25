from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    try:
        quantity = int(request.POST.get('quantity', 0))
        bag = request.session.get('bag', {})  # Example: Retrieving a bag from the session

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id, None)

        request.session['bag'] = bag  # Update the session
        messages.success(request, "Bag updated!")
        return redirect('view_bag')  # Adjust the redirect accordingly
    except Exception as e:
        messages.error(request, "There was an error updating the bag.")
        return redirect('view_bag')  # Adjust as necessary

def remove_from_bag(request, item_id):
    """Remove a product from the bag."""

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)

        # Update the session with the modified bag
        request.session['bag'] = bag
        messages.success(request, "Item removed from bag!")
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)