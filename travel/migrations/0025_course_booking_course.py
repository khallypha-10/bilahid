# Generated by Django 5.1.1 on 2024-09-16 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0024_remove_course_booking_availabilty'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_booking',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='travel.course'),
            preserve_default=False,
        ),
    ]
