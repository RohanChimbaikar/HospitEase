from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, unique=True)
    gender = models.CharField(max_length=10)
    class Meta:
        db_table = 'registration_registration'
    
    def __str__(self):
        return self.first_name + " " + self.last_name