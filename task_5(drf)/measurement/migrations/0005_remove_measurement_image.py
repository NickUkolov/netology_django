# Generated by Django 4.1.3 on 2022-11-15 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_options_alter_sensor_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='image',
        ),
    ]
