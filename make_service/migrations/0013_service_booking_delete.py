# Generated by Django 4.2.4 on 2024-02-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_service', '0012_service_booking_vehno'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_booking',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
