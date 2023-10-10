import pandas as pd
from django.http import HttpResponse
import xlwt
from django.shortcuts import render
from django.db.models import Count,Case,When,IntegerField
from home.models import Location, Product,Assignments, License, Device
# Create your views here.





def generalView(request):
    # Get a list of all distinct license names
    products = Product.objects.all() 
    distinct_license_names = License.objects.values_list('license_name', flat=True).distinct().order_by('product')

    # Query to get the number of each license applied to each location
    location_license_counts = Device.objects.filter(assgned_device__active=True).values(
        'location__location_name'
    ).annotate(
        **{
            f'{license_name.replace(" ", "")}': Count(Case(
                When(assgned_device__license__license_name=license_name, then=1),
                output_field=IntegerField(),
            )) for license_name in distinct_license_names
        }
    )


    if 'download_excel' in request.GET:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="license_counts.xls"'

        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('License Counts')

        # Write the table header
        worksheet.write(0, 0, 'Location')
        col = 1
        for license_name in distinct_license_names:
            worksheet.write(0, col, f'{license_name}')
            col += 1

        # Write the table data
        row = 1
        for item in location_license_counts:
            worksheet.write(row, 0, item['location__location_name'])
            col = 1
            
            for license_name in distinct_license_names:
                count_key = f'{license_name.replace(" ", "")}'
                worksheet.write(row, col, item.get(count_key, 0))
                col += 1
            row += 1

        workbook.save(response)
        return response

    context = {
        'location_license_counts': list(location_license_counts),
        'distinct_license_names': distinct_license_names,
        'products':products
    }
    

    return render(request, 'reports\generalview.html', context)

def testView(request):
      # Get all products
    products = Product.objects.all()

    # Get all locations
    locations = Location.objects.all()

    # Initialize an empty table list to hold the final result
    table_data = []

    # Loop through each location
    for location in locations:
        location_data = {
            'location': location,
            'product_data': [],
        }

        # Loop through each product
        for product in products:
            # Get all licenses associated with this product
            licenses = License.objects.filter(product=product)

            # Initialize a count for each license at this location
            license_count_per_location = {}

            # Loop through each license
            for license in licenses:
                # Use aggregation to count the number of devices with this license assigned at this location
                device_count = Assignments.objects.filter(device__location=location, license=license, active=True).count()

                # Add the count to the dictionary
                license_count_per_location[license.license_name] = device_count

            # Add the count of devices for each license at this location to the product_data list
            location_data['product_data'].append({
                'product': product,
                'license_count': license_count_per_location,
            })

        # Add the location data to the table_data list
        table_data.append(location_data)

    context = {
        'table_data': table_data,
    }
    return render(request,'reports/test.html',context)

