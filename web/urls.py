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
from bdsh_site import api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', api_views.LightCreate.as_view()),
    path('api/lightlamp/<int:lamp_id>/', api_views.LampView.as_view()),
    path('api/lightlamp/create/', api_views.LampCreate.as_view()),
    path('api/lightlamp/<int:lamp_id>/delete/', api_views.LampDelete.as_view()),
    path('api/lightsensor/<int:light_id>/', api_views.LightView.as_view()),
    path('api/lightsensor/create/', api_views.LightCreate.as_view()),
    path('api/lightsensor/<int:light_id>/delete/', api_views.LightDelete.as_view()),
]
