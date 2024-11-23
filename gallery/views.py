from django.shortcuts import render
from django.contrib import messages
from .models import Gallery

# Create your views here.


def gallery_gym(request):
    galleries = Gallery.objects.all()  # Queryset containing all Gallery objects
    return render(request, 'gallery/gallery.html', {'galleries': galleries})

