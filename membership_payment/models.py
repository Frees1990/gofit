from django.db import models
from django.contrib.auth.models import User
from membership.models import Membership

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    billing_address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_charge_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.membership.name}"

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    start_date = models.DateField()
    email = models.EmailField()
    is_active = models.BooleanField(default=True)


