# Generated by Django 5.0.2 on 2024-03-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
