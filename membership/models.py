from django.db import models

class Membership(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in months")
    description = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)  # Allows multiple lines of text

    def __str__(self):
        return self.name