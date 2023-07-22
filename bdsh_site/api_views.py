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
    def get(self, request, lamp_id):
        this_lamp = get_object_or_404(SensorData, id=lamp_id)
        if this_lamp.sensor_type != SensorTypes.LIGHTLAMP.value:
            return Response({'reason': 'This sensor is not light lamp'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_lamp)
        return Response(serializer.data)

    def post(self, request, lamp_id):
        this_lamp = get_object_or_404(SensorData, id=lamp_id)
        if this_lamp.sensor_type != SensorTypes.LIGHTLAMP.value:
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
        this_lamp.value = value_param
        this_lamp.save()

        return Response({'status': 'OK'})


class LampCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_lamp = SensorData(sensor_type=SensorTypes.LIGHTLAMP.value, value=0.0, board=esp)
        new_lamp.save()
        return Response({'status': 'OK', 'id': new_lamp.id})


class LampDelete(APIView):
    def post(self, request, lamp_id):
        this_lamp = get_object_or_404(SensorData, id=lamp_id)
        if this_lamp.sensor_type == SensorTypes.LIGHTLAMP.value:
            this_lamp.delete()
        else:
            return Response({'reason': 'This sensor is not lamp', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


class LightView(APIView):
    def get(self, request, light_id):
        this_light = get_object_or_404(SensorData, id=light_id)
        if this_light.sensor_type != SensorTypes.LIGHT_SENSOR.value:
            return Response({'reason': 'This sensor is not light sensor'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SensorDataSerializer(this_light)
        return Response(serializer.data)

    def post(self, request, light_id):
        this_light = get_object_or_404(SensorData, id=light_id)
        if this_light.sensor_type != SensorTypes.LIGHT_SENSOR.value:
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
        this_light.value = value_param
        this_light.save()

        return Response({'status': 'OK'})


class LightCreate(APIView):
    def post(self, request):
        ip = request.POST.get("ip", None)
        esp = get_object_or_404(ESP, ip=ip)
        new_light = SensorData(sensor_type=SensorTypes.LIGHT_SENSOR.value, value=0.0, board=esp)
        new_light.save()
        return Response({'status': 'OK', 'id': new_light.id})


class LightDelete(APIView):
    def post(self, request, light_id):
        this_light = get_object_or_404(SensorData, id=light_id)
        if this_light.sensor_type == SensorTypes.LIGHT_SENSOR.value:
            this_light.delete()
        else:
            return Response({'reason': 'This sensor is not light sensor', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})

