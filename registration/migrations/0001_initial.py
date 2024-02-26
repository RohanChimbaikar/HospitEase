# Generated by Django 5.0.2 on 2024-02-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
