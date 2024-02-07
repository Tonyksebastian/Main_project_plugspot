from django.contrib import admin
from .models import service_station,add_service,service_booking
# Register your models here.
admin.site.register(service_station)
admin.site.register(add_service)
admin.site.register(service_booking)

