from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from datetime import datetime
from user.models import *
fs=FileSystemStorage(location=settings.MEDIA_ROOT)

class Location(models.Model):

    vehicle_number = models.CharField(max_length=100)
    latitude=models.FloatField(blank=True,null=True)
    longitude=models.FloatField(blank=True,null=True)
    place_name=models.TextField(blank=True,null=True)
    known_location=models.BooleanField(default=False)
    altitude = models.FloatField(blank=True, null=True)
    bearing = models.FloatField(blank=True, null=True)
    direction=models.CharField(max_length=100,blank=True, null=True)
    time_recorded=models.DateTimeField(default=datetime.now,null=True)

    def __str__(self):
        return self.vehicle_number+"/"+str(self.time_recorded)

class image_vehicle(models.Model):
    vehicle_number = models.CharField(max_length=100)
    vehicle_pic=models.TextField(max_length=100000)
    time_recorded = models.DateTimeField(null=True)
    def __str__(self):
        return str(self.vehicle_number)

class Vehicle(models.Model):
    imei = models.CharField(max_length=100)
    owner=models.ForeignKey(AdminUser,on_delete=models.SET_NULL,null=True)
    driver=models.ForeignKey(AdminDriver,on_delete=models.SET_NULL,null=True)
    route=models.CharField(max_length=100)
    vehicle_number=models.CharField(max_length=100,unique=True)
    location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    running_status=models.BooleanField(default=False)
    # shifts=models.IntegerField(default=0,null=True)
    # parameters=models.ForeignKey(VehicleParameter,on_delete=models.SET_NULL,null=True)
    # obddata = models.OneToOneField(obd_data, on_delete=models.SET_NULL,null=True)
    installation_date = models.CharField(max_length=50,null=True)
    expiry_date = models.CharField(max_length=50,null=True)
    previous_latitude = models.FloatField(blank=True, null=True)
    previous_longitude = models.FloatField(blank=True, null=True)
    place_name=models.CharField(max_length=200,blank=True, null=True)
    distance_travel = models.FloatField(blank=True, null=True, default=0)
    type_of_device = models.CharField(max_length=100,null=True)
    # control=models.OneToOneField(Control,on_delete=models.SET_NULL,null=True)
    is_disconnected = models.BooleanField(default=False)
    imagevehicle = models.OneToOneField(image_vehicle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.vehicle_number