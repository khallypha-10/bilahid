# Generated by Django 5.1.1 on 2024-09-16 12:56

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0019_visa'),
    ]

    operations = [
        migrations.AddField(
            model_name='visa',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[400, 300], upload_to='visas'),
        ),
    ]
