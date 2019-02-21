from asn1crypto._ffi import null
from django.shortcuts import render,HttpResponse
from django.shortcuts import render, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time, threading
from datetime import datetime, timedelta,date
from django.contrib.auth import authenticate
import http.client
from django_otp.oath import totp
import time
from django.shortcuts import render,redirect
import base64
from track.models import *
import os
from geopy.distance import geodesic
from dateutil import parser



@csrf_exempt
def update_image(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        response_data = {}
        if post.get("key") == "ApkKzShan14752@$&kihgb14782**%##$$693opyhf%mod179fok6erttWQGF":
            image=post['image']
            # imgdata = base64.b64decode(image)

            try:
              vehicle= Vehicle.objects.get(imei=post['imei'])
              time_recorded = datetime.now()
              img, created = image_vehicle.objects.get_or_create(vehicle_number=vehicle.vehicle_number)
              img.time_recorded = time_recorded
              img.vehicle_pic = image
              img.save()

            # try:
            #   vehicle = Vehicle.objects.get(vehicle_number=vehicle_nu)
            #   path=''
            #   BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            #   ark = str(BASE_PATH).split('/')
            #   for i in range(0, len(ark) - 1):
            #       path = path + ark[i] + "/"
            #   image_directory = path + "IMAGE_RECORD/"+vehicle.owner_name+"/"+vehicle_nu+"/"+str(datetime.now().date())
            #   filename=image_directory+"/"+(datetime.now().strftime("%H:%M:%S"))+".jpeg"
            #   print(filename)
            #   if not os.path.exists(image_directory):
            #     try:
            #       os.mkdir(image_directory)
            #     except:
            #       os.makedirs(image_directory)
            #
            #   fh = open(filename, "wb")
            #   fh.write(imgdata)
            #   fh.close()
            except Exception as e:
              print (e)
              pass
            del image
            del post
            response_data['status']="success"
        else:
          response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")


@csrf_exempt
def liveLocation(request):
    response={}
    if request.method=="POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        if post['key']=="ApkKzShan14752@$&kihgb14782**%##$$693opyhf%mod179fok6erttWQGF":
            try:

                vehicle=Vehicle.objects.get(imei=post['imei'])
                location=Location()
                location.vehicle_number=vehicle.vehicle_number
                location.latitude=post['latitude']
                location.longitude=post['longitude']
                location.place_name=post['address']
                # location.altitude=post['altitude']
                # location.bearing=post['bearing']
                # location.direction=bearing_show(float(post['bearing']))
                location.time_recorded= datetime.strptime(post['date'], '%d/%m/%Y %H:%M:%S')
                location.save()
                vehicle.running_status=True
                vehicle.location=location
                vehicle.save()

            except Exception as e:
                print(e)
            response['status']="success"


        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
         raise Http404("NOT ALLOWED")


def bearing_show(bearing):

  print(bearing)
  try:
        if 0.0<=bearing <=30.0 or 330.0<=bearing<=360.0:
          return  "NORTH"

        elif 30.0 <= bearing<=60.0:

            return "EAST-NORTH"
        elif 300.0 <= bearing<=330.0:

            return "NORTH-WEST"
        elif 240.0 <= bearing<=300.0:
            return "WEST"
        elif 210.0 <= bearing<=240.0:

            return "SOUTH-WEST"
        elif 150.0 <= bearing<=210.0:

            return "SOUTH"
        elif 120.0 <= bearing<=150.0:

            return "SOUTH-EAST"
        elif 60.0 <= bearing <= 120.0:

            return "EAST"
  except Exception as e:
    print (e)
    return "null"






@csrf_exempt
def vehicleValue(request):
    value={}
    index=0

    print(request.GET['user'])
    user=AdminUser.objects.get(username=request.GET['user'])
    vehicle=Vehicle.objects.filter(owner=user).order_by('location').reverse()
    for car in vehicle:



             value[index]={'number':car.vehicle_number,
                           'address':car.location.place_name,
                           'update':car.location.time_recorded.strftime("%H:%M:%S %d/%m/%Y"),
                           'status':car.running_status,



             }
             index+=1


    return HttpResponse(json.dumps(value), content_type="application/json")


@csrf_exempt
def valueCar(request):
    value={}
    car = Vehicle.objects.get(vehicle_number=request.GET['car'])
    value={
        'number': car.vehicle_number,
        'address': car.location.place_name,
        'update': car.location.time_recorded.strftime("%H:%M:%S %d/%m/%Y"),
        'status': car.running_status,
        'latitute':car.location.latitude,
        'longitute':car.location.longitude,
        'camera':car.imagevehicle.vehicle_pic,
    }



    return HttpResponse(json.dumps(value), content_type="application/json")




@csrf_exempt
def data_pah(request):
        response_data = {}

        path = {}
        data = {}
        index = 0
        prelan = 0.0
        prelong = 0.0
        prevdate = datetime.now()
        locat = Location.objects.filter(vehicle_number=request.GET['vehicle'],time_recorded__startswith=parser.parse(request.GET['choice']).date()).order_by('time_recorded')

        for location in locat:
              if (location.latitude!=null and location.longitude!=null and location.latitude!=0 and location.longitude!=0):
                    if prelan == 0.0 and prelong == 0.0:
                        data = {
                            "vehicle_number": request.GET['vehicle'],
                            "latitude": location.latitude,
                            "longitude": location.longitude,
                            "place": location.place_name,
                            "time_recorded": location.time_recorded.strftime("%d-%m-%Y-%H-%M-%S"),
                        }
                        prelan = location.latitude
                        prelong = location.longitude
                        prevdate = location.time_recorded

                    else:
                        previous_location = [prelan, prelong]
                        vehicle_location = [location.latitude, location.longitude]
                        c = geodesic(previous_location, vehicle_location)

                        interval = (location.time_recorded - prevdate).seconds / 3600
                        if interval == 0:
                            continue
                        speed = c.km / interval
                        if speed < 80:
                            data = {
                                "vehicle_number": request.GET['vehicle'],
                                "latitude": location.latitude,
                                "longitude": location.longitude,

                                "place": location.place_name,
                                "time_recorded": location.time_recorded.strftime("%d-%m-%Y-%H-%M-%S"),
                            }

                            prelan = location.latitude
                            prelong = location.longitude
                            prevdate = location.time_recorded
                        else:

                            continue

                    path[index] = data
                    index += 1
        response_data[0] = path

        return HttpResponse(json.dumps(response_data), content_type="application/json")








@csrf_exempt
def daily_pah(request):
        response_data = {}

        path = {}
        data = {}
        index = 0
        prelan = 0.0
        prelong = 0.0
        prevdate = datetime.now()
        locat = Location.objects.filter(vehicle_number=request.GET['vehicle'],time_recorded__startswith=datetime.now().date()).order_by('time_recorded')

        for location in locat:
              if (location.latitude!=null and location.longitude!=null and location.latitude!=0 and location.longitude!=0):
                    if prelan == 0.0 and prelong == 0.0:
                        data = {
                            "vehicle_number": request.GET['vehicle'],
                            "latitude": location.latitude,
                            "longitude": location.longitude,
                            "place": location.place_name,
                            "time_recorded": location.time_recorded.strftime("%d-%m-%Y-%H-%M-%S"),
                        }
                        prelan = location.latitude
                        prelong = location.longitude
                        prevdate = location.time_recorded

                    else:
                        previous_location = [prelan, prelong]
                        vehicle_location = [location.latitude, location.longitude]
                        c = geodesic(previous_location, vehicle_location)

                        interval = (location.time_recorded - prevdate).seconds / 3600
                        if interval == 0:
                            continue
                        speed = c.km / interval
                        if speed < 80:
                            data = {
                                "vehicle_number": request.GET['vehicle'],
                                "latitude": location.latitude,
                                "longitude": location.longitude,

                                "place": location.place_name,
                                "time_recorded": location.time_recorded.strftime("%d-%m-%Y-%H-%M-%S"),
                            }

                            prelan = location.latitude
                            prelong = location.longitude
                            prevdate = location.time_recorded
                        else:

                            continue

                    path[index] = data
                    index += 1
        response_data[0] = path

        return HttpResponse(json.dumps(response_data), content_type="application/json")




def location_delet(request):
    for lot in Location.objects.all():
        lot.delete()