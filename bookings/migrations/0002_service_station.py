# Generated by Django 4.2.4 on 2024-01-23 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.CharField(default='', max_length=30)),
                ('ownername', models.CharField(default='', max_length=25)),
                ('place', models.CharField(default='', max_length=30)),
                ('photo', models.ImageField(default='', upload_to='pic')),
                ('latitude', models.CharField(max_length=12, null=True)),
                ('longitude', models.CharField(max_length=12, null=True)),
                ('maxslot', models.IntegerField(default='4')),
                ('description', models.CharField(default='', max_length=250)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('available', models.IntegerField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
