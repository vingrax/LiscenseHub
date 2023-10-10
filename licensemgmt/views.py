from django.shortcuts import redirect, render
from home.models import Device,License,Assignments,Product
from django.http import JsonResponse
from django.utils.timezone import now
from django.db import transaction
import json

# Create your views here.
def devicesView(request):
    #Initial Render
    return render(request,'licensemgmt/devices.html')


def search(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        search_input = payload.get('searchInput')
        search_by = payload.get('searchType')
        
        if search_by == 'DNS':
            devices = Device.objects.filter(dns_name__icontains=search_input)
        else:
            devices = Device.objects.filter(ip__icontains=search_input)
        
        # Convert devices queryset to a list of dictionaries
        device_list = []
        for device in devices:
            device_list.append({
                'dns_name': device.dns_name,
                'ip': device.ip,
                # Add other device properties as needed
            })
        
        # Return the device list as a JSON response
        return JsonResponse(device_list, safe=False)

def deviceView(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        deviceip = payload.get("deviceIP")
        device = Device.objects.get(ip =deviceip)
        print(device)
        context = {
            'device':device
        }
        return render(request,"licensemgmt/viewdevice.html",context)


                        

def manage_license(request, device_ip):
    devicen = Device.objects.get(ip=device_ip)
    products = Product.objects.all()



    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            license_ids = request.POST.getlist('licenses')
            licenses = License.objects.filter(id__in=license_ids)

            # Create a list to store the new assignments
            new_assignments = []

            # Decrement the license_count for each assigned license
            for license in licenses:
                license.license_count -= 1
                license.save()

                # Create an assignment instance with the selected license
                assignment = Assignments(
                    license=license,
                    device=devicen,
                    remarks=request.POST.get('remarks-' + str(license.id))
                )
                new_assignments.append(assignment)

            # Bulk create the new assignments
            with transaction.atomic():
                Assignments.objects.bulk_create(new_assignments)


        if(action == 'remove'):
            license_ids = request.POST.getlist('licenses[]')
            assignments = Assignments.objects.filter(id__in=license_ids)
            assignments.update(active=False,removed_date=now())
            print('Licenses removed')

    licenses = License.objects.all()
    return render(request, 'licensemgmt/addlicense.html', {'device': devicen, 'licenses': licenses, 'products': products})

