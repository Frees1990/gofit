from django.utils import timezone
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Classes, day


def all_classes(request):
    """ A view to show all classes """

    classes = Classes.objects.all()
    classes = Classes.objects.filter(end_time__date__gte=today)
    today = timezone.now().date()
    query = None
    days = None


    if 'day' in request.GET:
        days = request.GET['day'].split(',')
        classes = classes.filter(category__name__in=days)
        days = Day.objects.filter(name__in=days)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('classes'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            classes = classes.filter(queries)

    context = {
        'classes': classes,
        'search_term': query,
        'day': day,
    }

    return render(request, 'classes/classes.html', context)