from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_view, name='payment_view'),
    path('payment/success/', views.success_view, name='payment_success'),
]
