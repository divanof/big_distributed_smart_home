from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bdsh_site.models import SensorData
from bdsh_site.serializers import SensorDataSerializer


def index_page(request):
    return render(request, 'index.html')


def settings_page(request):
    return render(request, 'settings.html')


def login_page(request):
    return render(request, 'login.html')


def switch_page(request):
    context = {'sensor_id': 1}
    return render(request, 'switch_light.html', context)


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
        print(request.POST.keys())
        value_param = request.POST.get('value', None)
        from_param = request.POST.get('from', None)

        if value_param is None:
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param is None:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if int(value_param) not in [0, 1]:
            print(value_param)
            return Response({'reason': 'Invalid value param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        if from_param not in ['user', 'sensor']:
            return Response({'reason': 'Invalid from param', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
        this_lamp.value = value_param
        this_lamp.save()

        return Response({'status': 'OK'})
