# Generated by Django 5.1.1 on 2024-09-15 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_payments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_booking',
            name='message',
        ),
    ]
