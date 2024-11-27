from django.db import models
from django.conf import settings

class Membership(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.membership.name if self.membership else 'No Membership'}"
