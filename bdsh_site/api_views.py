from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from bdsh_site.models import SensorData, ESP, SensorTypes
from bdsh_site.serializers import SensorDataSerializer


def index(request):
    return HttpResponse("lorem")


class LampView(APIView):
    def get(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.LIGHTLAMP.value:
            return Response({'reason': 'This sensor is not light lamp'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_sensor)
        return Response(serializer.data)

    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.LIGHTLAMP.value:
            return Response({'reason': 'This sensor is not light lamp'}, status=status.HTTP_400_BAD_REQUEST)
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        value_param = 1 if float(value_param) > 0.5 else 0
        if value_param not in [0, 1]:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_sensor.value = value_param
        this_sensor.save()

        return Response({'status': 'OK'})


class LampCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_sensor = SensorData(sensor_type=SensorTypes.LIGHTLAMP.value, value=0.0, board=esp)
        new_sensor.save()
        return Response({'status': 'OK', 'id': new_sensor.id})


class LampDelete(APIView):
    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type == SensorTypes.LIGHTLAMP.value:
            this_sensor.delete()
        else:
            return Response({'reason': 'This sensor is not lamp', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


class LightView(APIView):
    def get(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.LIGHT_SENSOR.value:
            return Response({'reason': 'This sensor is not light sensor'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_sensor)
        return Response(serializer.data)

    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.LIGHT_SENSOR.value:
            return Response({'reason': 'This sensor is not light sensor'}, status=status.HTTP_400_BAD_REQUEST)
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        value_param = float(value_param)
        if value_param < 0 or value_param > 99:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_sensor.value = value_param
        this_sensor.save()

        return Response({'status': 'OK'})


class LightCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_sensor = SensorData(sensor_type=SensorTypes.LIGHT_SENSOR.value, value=0.0, board=esp)
        new_sensor.save()
        return Response({'status': 'OK', 'id': new_sensor.id})


class LightDelete(APIView):
    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type == SensorTypes.LIGHT_SENSOR.value:
            this_sensor.delete()
        else:
            return Response({'reason': 'This sensor is not light sensor', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


class ReedView(APIView):
    def get(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.REED.value:
            return Response({'reason': 'This sensor is not reed'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_sensor)
        return Response(serializer.data)

    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.REED.value:
            return Response({'reason': 'This sensor is not reed'}, status=status.HTTP_400_BAD_REQUEST)
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        value_param = 1 if float(value_param) > 0.5 else 0
        if value_param not in [0, 1]:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_sensor.value = value_param
        this_sensor.save()

        return Response({'status': 'OK'})


class ReedCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_sensor = SensorData(sensor_type=SensorTypes.REED.value, value=0.0, board=esp)
        new_sensor.save()
        return Response({'status': 'OK', 'id': new_sensor.id})


class ReedDelete(APIView):
    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type == SensorTypes.REED.value:
            this_sensor.delete()
        else:
            return Response({'reason': 'This sensor is not reed', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


class TempView(APIView):
    def get(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.TEMPERATURE_SENSOR.value:
            return Response({'reason': 'This sensor is not temperature sensor'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_sensor)
        return Response(serializer.data)

    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.TEMPERATURE_SENSOR.value:
            return Response({'reason': 'This sensor is not temperature sensor'}, status=status.HTTP_400_BAD_REQUEST)
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        value_param = float(value_param)
        if value_param < 0 or value_param > 40:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_sensor.value = value_param
        this_sensor.save()

        return Response({'status': 'OK'})


class TempCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_sensor = SensorData(sensor_type=SensorTypes.TEMPERATURE_SENSOR.value, value=0.0, board=esp)
        new_sensor.save()
        return Response({'status': 'OK', 'id': new_sensor.id})


class TempDelete(APIView):
    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type == SensorTypes.TEMPERATURE_SENSOR.value:
            this_sensor.delete()
        else:
            return Response({'reason': 'This sensor is not temperature sensor', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


class HumView(APIView):
    def get(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.HUMIDITY_SENSOR.value:
            return Response({'reason': 'This sensor is not humidity sensor'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_sensor)
        return Response(serializer.data)

    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.HUMIDITY_SENSOR.value:
            return Response({'reason': 'This sensor is not humidity sensor'}, status=status.HTTP_400_BAD_REQUEST)
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        value_param = float(value_param)
        if value_param < 0 or value_param > 100:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_sensor.value = value_param
        this_sensor.save()

        return Response({'status': 'OK'})


class HumCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_sensor = SensorData(sensor_type=SensorTypes.HUMIDITY_SENSOR.value, value=0.0, board=esp)
        new_sensor.save()
        return Response({'status': 'OK', 'id': new_sensor.id})


class HumDelete(APIView):
    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type == SensorTypes.HUMIDITY_SENSOR.value:
            this_sensor.delete()
        else:
            return Response({'reason': 'This sensor is not humidity sensor', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


class LeakageView(APIView):
    def get(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.LEAKAGE_SENSOR.value:
            return Response({'reason': 'This sensor is not leakage sensor'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_sensor)
        return Response(serializer.data)

    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type != SensorTypes.LEAKAGE_SENSOR.value:
            return Response({'reason': 'This sensor is not leakage sensor'}, status=status.HTTP_400_BAD_REQUEST)
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        value_param = float(value_param)
        if value_param < 0 or value_param > 100:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_sensor.value = value_param
        this_sensor.save()

        return Response({'status': 'OK'})


class LeakageCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_sensor = SensorData(sensor_type=SensorTypes.LEAKAGE_SENSOR.value, value=0.0, board=esp)
        new_sensor.save()
        return Response({'status': 'OK', 'id': new_sensor.id})


class LeakageDelete(APIView):
    def post(self, request, sensor_id):
        this_sensor = get_object_or_404(SensorData, id=sensor_id)
        if this_sensor.sensor_type == SensorTypes.LEAKAGE_SENSOR.value:
            this_sensor.delete()
        else:
            return Response({'reason': 'This sensor is not leakage sensor', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


class DeviceView(APIView):
    def get(self, request):
        ip = request.GET.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        sensors = SensorData.objects.filter(board=esp)
        serializer = SensorDataSerializer(sensors, many=True)
        return Response(serializer.data)
