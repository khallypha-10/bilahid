# Generated by Django 5.1.1 on 2024-09-16 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0023_tour_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_booking',
            name='availabilty',
        ),
    ]
