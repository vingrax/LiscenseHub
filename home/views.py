from django.shortcuts import render
from django.http import HttpResponse
from .models import Device,License,User

# Create your views here.
def homeView(request):
    #send all devices as context
    licenses = License.objects.count()
    devices = Device.objects.count()
    context={
        'licenses':licenses,
        'devices':devices,
    }
     
    
    return render(request,'home/homepage.html',context)