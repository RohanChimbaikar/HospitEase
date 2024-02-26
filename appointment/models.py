# Create your models here.
from django.db import models

class Appointment(models.Model):
    doctor_choices = [
        ('Dr. Smith', 'Dr. Smith - Cardiology'),
        ('Dr. Johnson', 'Dr. Johnson - Neurology'),
        ('Dr. Lee', 'Dr. Lee - Pediatrics'),
    ]
    doctor = models.CharField(max_length=100, choices=doctor_choices)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time} for {self.name}"
