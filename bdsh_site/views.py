from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bdsh_site.models import SensorData, ESP
from bdsh_site.serializers import SensorDataSerializer


def index(request):
    return HttpResponse("lorem")


@api_view(['GET', 'POST'])
def lamp(request, lamp_id):
    try:
        this_lamp = SensorData.objects.get(id=lamp_id)
    except SensorData.DoesNotExist:
        return Response({'reason': 'Invalid lamp id'}, status=status.HTTP_404_NOT_FOUND)
    if this_lamp.sensor_type != 1:
        return Response({'reason': 'This sensor is not light lamp'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = SensorDataSerializer(this_lamp)
        return Response(serializer.data)

    elif request.method == 'POST':
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if int(value_param) not in [0, 1]:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_lamp.value = value_param
        this_lamp.save()

        return Response({'status': 'OK'})


@api_view(['GET', 'POST'])
def lamp_create(request):
    if request.method == "POST":
        ip = request.POST.get("ip", None)
        if ip is None:
            return Response({'reason': 'Invalid ip param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        try:
            esp = ESP.objects.get(ip=ip)
        except ESP.DoesNotExist:
            return Response({'reason': 'Invalid ip param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        new_lamp = SensorData(sensor_type=1, value=0.0, board=esp)
        new_lamp.save()
        return Response({'status': 'OK'})


@api_view(['POST'])
def lamp_delete(request, lamp_id):
    if request.method == "POST":
        try:
            this_lamp = SensorData.objects.get(id=lamp_id)
        except SensorData.DoesNotExist:
            return Response({'reason': 'Invalid lamp id param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if this_lamp.sensor_type == 1:
            this_lamp.delete()
        else:
            return Response({'reason': 'This sensor is not lamp', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'OK'})


@api_view(['GET', 'POST'])
def light(request, light_sensor_id):
    try:
        this_light = SensorData.objects.get(id=light_sensor_id)
    except SensorData.DoesNotExist:
        return Response({'reason': 'Invalid light sensor id'}, status=status.HTTP_404_NOT_FOUND)
    if this_lamp.sensor_type != 2:
        return Response({'reason': 'This sensor is not light sensor'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = SensorDataSerializer(this_light)
        return Response(serializer.data)

    elif request.method == 'POST':
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if value_param < 0 or value_param > 99:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_lamp.value = value_param
        this_lamp.save()

        return Response({'status': 'OK'})
