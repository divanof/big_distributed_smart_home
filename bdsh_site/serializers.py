from bdsh_site.models import SensorData
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'sensor_type', 'value']
