"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bdsh_site import views, api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lightlamp/<int:sensor_id>/', api_views.LampView.as_view()),
    path('api/lightlamp/create/', api_views.LampCreate.as_view()),
    path('api/lightlamp/<int:sensor_id>/delete/', api_views.LampDelete.as_view()),
    path('api/light/<int:sensor_id>/', api_views.LightView.as_view()),
    path('api/light/create/', api_views.LightCreate.as_view()),
    path('api/light/<int:sensor_id>/delete/', api_views.LightDelete.as_view()),
    path('api/reed/<int:sensor_id>/', api_views.ReedView.as_view()),
    path('api/reed/create/', api_views.ReedCreate.as_view()),
    path('api/reed/<int:sensor_id>/delete/', api_views.ReedDelete.as_view()),
    path('api/temp/<int:sensor_id>/', api_views.TempView.as_view()),
    path('api/temp/create/', api_views.TempCreate.as_view()),
    path('api/temp/<int:sensor_id>/delete/', api_views.TempDelete.as_view()),
    path('api/humidity/<int:sensor_id>/', api_views.HumView.as_view()),
    path('api/humidity/create/', api_views.HumCreate.as_view()),
    path('api/humidity/<int:sensor_id>/delete/', api_views.HumDelete.as_view()),
    path('api/leakage/<int:sensor_id>/', api_views.LeakageView.as_view()),
    path('api/leakage/create/', api_views.LeakageCreate.as_view()),
    path('api/leakage/<int:sensor_id>/delete/', api_views.LeakageDelete.as_view()),
    path('api/get_device/', api_views.DeviceView.as_view())
]
