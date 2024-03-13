# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    # Assuming you're using the default User model
    doctor_choices = [
        ('Dr. Smith', 'Dr. Smith - Cardiology'),
        ('Dr. Johnson', 'Dr. Johnson - Neurology'),
        ('Dr. Lee', 'Dr. Lee - Pediatrics'),
        ('Dr .Leo','Dr. Leo - X-Ray'),
    ]
    doctor = models.ForeignKey(User, on_delete=models.CASCADE,choices=doctor_choices)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time} for {self.name}"