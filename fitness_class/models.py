from django.db import models
from django.contrib.auth.models import User

class FitnessClass(models.Model):
    CLASS_DAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]
    
    name = models.CharField(max_length=200)
    day = models.CharField(max_length=9, choices=CLASS_DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} on {self.day} from {self.start_time} to {self.end_time}"
