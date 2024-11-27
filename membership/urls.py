from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_list, name='membership_list'),
    path('select/', views.select_membership, name='select_membership'),
    path('confirmation/', views.membership_confirmation, name='membership_confirmation'),
]