from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_list, name='membership_list'),
    path('select/', views.select_membership, name='select_membership'),
    path('confirmation/', views.membership_confirmation, name='membership_confirmation'),
    path('add/', views.add_membership, name='add_membership'),
    path('edit/<int:membership_id>/', views.edit_membership, name='edit_membership'),
    path('delete/<int:membership_id>/', views.delete_membership, name='delete_membership'),
]