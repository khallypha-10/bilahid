# Generated by Django 5.1.1 on 2024-09-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
