from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_list, name='membership_list'),
    path('detail/<int:membership_id>/', views.membership_detail, name='membership_detail'),
    path('add/', views.add_membership, name='add_membership'),
    path('edit/<int:membership_id>/', views.edit_membership, name='edit_membership'),
    path('delete/<int:membership_id>/', views.delete_membership, name='delete_membership'),
]