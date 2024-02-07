from django.db import models
from userapp.models import CustomUser

# Create your models here.
class service_station(models.Model):
    stname = models.CharField(max_length=30, default='')
    ownername = models.CharField(default='', max_length=25)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    place = models.CharField(default='', max_length=30)
    photo = models.ImageField(upload_to='pic', default='')
    latitude = models.CharField(max_length=12,null=True)
    longitude = models.CharField(max_length=12,null=True)
    maxslot = models.IntegerField(default='4')
    description = models.CharField(default='', max_length=250)
    contact = models.IntegerField(null=True,blank=True)
    date = models.DateField(null=True)
    hidden = models.BooleanField(default=False)
    available=models.IntegerField(null=True)
    status= models.BooleanField(default=False)

    def __str__(self):
        return str(self.stname)
    
class add_service(models.Model):
    photo = models.ImageField(upload_to='pic', default='')
    ser_name = models.CharField(max_length=30, default='')
    description = models.CharField(default='', max_length=250)
    price = models.FloatField()
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='service_by_name', null=True)
    service=models.ForeignKey(service_station,null=True,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

class CarService(models.Model):
    name = models.CharField(max_length=55, unique=True)

class service_booking(models.Model):
    ownername = models.CharField(default='', max_length=25, null=True)
    phone = models.IntegerField(null=True,blank=True)
    company = models.CharField(default='', max_length=250)
    model = models.CharField(default='', max_length=250)
    km_done = models.FloatField()
    vehno = models.CharField(default='', max_length=250)
    date = models.DateTimeField()
    type = models.CharField(default='', max_length=25)
    status = models.BooleanField(default=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='service_book', null=True)
    car_services = models.ManyToManyField(CarService, related_name='service_bookings')