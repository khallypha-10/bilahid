# Generated by Django 5.1.1 on 2024-09-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_itinerary_image_1_itinerary_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='overview',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ut nibh non magna luctus placerat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque ut molestie mi. Etiam molestie volutpat tellus ac sodales. Maecenas scelerisque dolor massa, eget semper mauris vestibulum id. Donec fringilla accumsan aliquet. Praesent ornare dolor est, et sodales quam fringilla sit amet.'),
            preserve_default=False,
        ),
    ]
