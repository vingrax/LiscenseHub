from django.db import models
from django.utils.timezone import now

class Company(models.Model):
    company_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'company'
    def __str__(self):
        return self.company_name

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'location'
    def __str__(self):
        return self.location_name    
        

class Division(models.Model):
    division_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'division'
    def __str__(self):
        return self.division_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    class Meta:
        db_table = 'department'
    def __str__(self):
        return self.department_name
class User(models.Model):
    employee_number = models.CharField(max_length=20)
    user_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.user_name
class Device(models.Model):
    DEVICE_TYPES = (
        ('PC', 'PC'),
        ('Laptop', 'Laptop'),
        ('TC', 'Thin Client'),
    )
    OS_TYPES = (
        ('Windows', 'Windows'),
        ('MAC', 'Mac'),
    )
    CONNECTION_TYPES = (
        ('LAN', 'LAN'),
        ('Wifi', 'Wifi'),
    )

    dns_name = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    os_type = models.CharField(max_length=20, choices=OS_TYPES)
    os_version = models.CharField(max_length=100)
    os_name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    product_key_last_part = models.CharField(max_length=100)
    network_connection_type = models.CharField(max_length=100,choices=CONNECTION_TYPES)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='devices')

    class Meta:
        db_table = 'device'
    def __str__(self):
        return self.dns_name



class Product(models.Model):
    product_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product'
    def __str__(self):
        return self.product_name

class License(models.Model):
    LICENSE_TYPES = (
        ('User License', 'User License'),
        ('Device License', 'Device License'),
    )

    license_type = models.CharField(max_length=100, choices=LICENSE_TYPES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='license_set')
    license_name = models.CharField(max_length=100)
    license_count = models.IntegerField()

    class Meta:
        db_table = 'license'
    def __str__(self):
        return self.license_name

class Assignments(models.Model):
    license = models.ForeignKey(License,on_delete=models.CASCADE,related_name='assgnd_license')
    device = models.ForeignKey(Device,on_delete=models.CASCADE,related_name='assgned_device')    
    remarks = models.TextField(max_length=1000,null=True,blank=True)
    active = models.BooleanField(default=True)
    assgnd_date = models.DateField( null=False,default=now)
    removed_date = models.DateField( null=True)
    expiry_date = models.DateField(null=True)
    
    class Meta:
        db_table = 'assignments'

        