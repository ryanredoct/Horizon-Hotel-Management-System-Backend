# Generated by Django 4.2.20 on 2025-03-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='amenities',
            field=models.TextField(blank=True, help_text='Comma-separated list of amenities', null=True),
        ),
    ]
