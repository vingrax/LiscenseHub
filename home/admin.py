from django.contrib import admin
from . import models

admin.site.site_header = "LicenseHub Administration"
admin.site.site_title = "LicenseHub Admin Portal"
admin.site.index_title = "Welcome to LicenseHub Administration"

# Register your models here.
admin.site.register(models.Location)
admin.site.register(models.License)
admin.site.register(models.Division)
admin.site.register(models.Device)
admin.site.register(models.Department)
admin.site.register(models.User)
admin.site.register(models.Company)
admin.site.register(models.Product)
admin.site.register(models.Assignments)