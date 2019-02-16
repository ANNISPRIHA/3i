from django.conf.urls import url
from django.contrib import admin

from . views import *
urlpatterns = [
    url(r'^liveLocation/', liveLocation),
    url(r'^update_image/', update_image),
    url(r'^vehicleValue/', vehicleValue),
    url(r'^valueCar/', valueCar),
    url(r'^location_delet/', location_delet),
url(r'^data_pah/', data_pah),
url(r'^daily_pah/', daily_pah),
]