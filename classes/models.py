from django.db import models
from django.contrib.auth.models import User


class day(models.Model):

    class Meta:
        verbose_name_plural = 'Days'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class classes(models.Model):
    day = models.ForeignKey('Day', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_participants = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.start_time}"