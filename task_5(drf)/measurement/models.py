from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'sensor'
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'measurement'
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
