from django.db import models

from enum import Enum


class SensorTypes(Enum):
    LIGHTLAMP = 1
    LIGHT_SENSOR = 2
    REED = 3
    TEMPERATURE_SENSOR = 4
    HUMIDITY_SENSOR = 5
    LEAKAGE_SENSOR = 6


class ESP(models.Model):
    ip = models.GenericIPAddressField(null=True, unique=True)


class SensorData(models.Model):
    """
    sensor types:
        1: light lamp
        2: light sensor
        3: reed
        4: temperature sensor
        5: humidity sensor
        6: leakage sensor
    """
    sensor_type = models.IntegerField(default=-1)
    value = models.FloatField()
    board = models.ForeignKey(to=ESP, on_delete=models.CASCADE)
