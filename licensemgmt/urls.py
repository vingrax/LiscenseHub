from django.urls import path
from . import views

urlpatterns = [
    path('devices/',views.devicesView,name="managedevices"),
    path('search/',views.search),
    path('device/',views.deviceView,name="viewdevice"),
    path('device/<str:device_ip>/manage_license/', views.manage_license, name='manage_license')
]
