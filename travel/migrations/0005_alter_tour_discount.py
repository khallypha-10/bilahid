# Generated by Django 5.1.1 on 2024-09-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_tour_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='discount',
            field=models.IntegerField(blank=True, help_text='in %', null=True),
        ),
    ]
