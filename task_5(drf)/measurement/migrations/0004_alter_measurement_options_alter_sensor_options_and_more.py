# Generated by Django 4.1.3 on 2022-11-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Сенсор', 'verbose_name_plural': 'Сенсоры'},
        ),
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='measurement',
            table='measurement',
        ),
        migrations.AlterModelTable(
            name='sensor',
            table='sensor',
        ),
    ]
