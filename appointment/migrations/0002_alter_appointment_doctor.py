# Generated by Django 5.0.2 on 2024-03-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(choices=[('Dr. Smith', 'Dr. Smith - Cardiology'), ('Dr. Johnson', 'Dr. Johnson - Neurology'), ('Dr. Lee', 'Dr. Lee - Pediatrics'), ('Dr .Leo', 'Dr.Leo - X')], max_length=100),
        ),
    ]
