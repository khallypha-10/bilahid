# Generated by Django 5.1.1 on 2024-09-14 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_tour_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itinerary',
            options={'verbose_name_plural': 'Itineraries'},
        ),
    ]
