# Generated by Django 5.1.1 on 2024-09-15 12:39

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('availabilty', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
