from . import views
from django.urls import path

urlpatterns = [
    path('gallery/', views.gallery_gym, name='gallery'),
]