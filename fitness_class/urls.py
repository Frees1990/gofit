# fitness_class/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_schedule, name='class_schedule'),  # List all classes
    path('add/', views.add_class, name='add_class'),  # Add new class
    path('edit/<int:class_id>/', views.edit_class, name='edit_class'),  # Edit class
    path('delete/<int:class_id>/', views.delete_class, name='delete_class'),  # Delete class
    path('book/<int:class_id>/', views.book_class, name='book_class'),
]
