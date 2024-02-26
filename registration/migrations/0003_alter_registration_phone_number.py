# Generated by Django 5.0.2 on 2024-02-14 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_registration_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]