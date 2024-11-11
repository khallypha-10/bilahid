# Generated by Django 5.1.1 on 2024-09-14 23:04

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_alter_tour_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('amenity_1', models.CharField(blank=True, max_length=100, null=True)),
                ('amenity_2', models.CharField(blank=True, max_length=100, null=True)),
                ('amenity_3', models.CharField(blank=True, max_length=100, null=True)),
                ('amenity_4', models.CharField(blank=True, max_length=100, null=True)),
                ('amenity_5', models.CharField(blank=True, max_length=100, null=True)),
                ('amenity_6', models.CharField(blank=True, max_length=100, null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[400, 300], upload_to='tour_hotel')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.tour')),
            ],
            options={
                'verbose_name_plural': 'Tour Hotels',
            },
        ),
    ]
