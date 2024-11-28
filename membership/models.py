from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in months")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.membership.name}"