# Generated by Django 4.2.4 on 2024-02-01 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_service', '0006_alter_service_booking_ownername'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_booking',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
