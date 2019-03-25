

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from.models import *
from track.models import *
from datetime import datetime, timedelta,date
import os
import cv2
from geopy.distance import geodesic
from geopy.geocoders import GoogleV3
import requests
import json
logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(hour=00, minute=10,)),name="show",gnore_result=True)
def show():
    print("boom lol")
    path = ''
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ark = str(BASE_PATH).split('/')
    for i in range(0, len(ark) - 1):
          path = path + ark[i] + "/"
    image_directory = path + "IMAGE_RECORD/"

    for vehicle in Vehicle.objects.all():
        vehicle_directory = image_directory + vehicle.owner_name + "/" + vehicle.vehicle_number
        date_wise_directory = vehicle_directory + "/" + str(datetime.now().date())
        if not os.path.exists(vehicle_directory):
            try:
                os.mkdir(vehicle_directory)
            except:
                os.makedirs(vehicle_directory)
        if not os.path.exists(date_wise_directory):
            try:
                os.mkdir(date_wise_directory)
            except:
                os.makedirs(date_wise_directory)


        date_wise_directory = vehicle_directory + "/" + str((datetime.now() - timedelta(days=1)).date())

        image_folder = date_wise_directory
        video_name = date_wise_directory + "/" + vehicle.vehicle_number + '.mp4'  # save as .avi

        images = []
        try:
            for f in sorted(os.listdir(image_folder)):
                if f.endswith('jpeg'):
                    images.append(f)
            if len(images) > 0:
            # Determine the width and height from the first image
                image_path = os.path.join(image_folder, images[0])
                frame = cv2.imread(image_path)
                cv2.imshow('video', frame)
                height, width, channels = frame.shape

                # Define the codec and create VideoWriter object
                fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')  # Be sure to use lower case
                out = cv2.VideoWriter(video_name, fourcc, 0.5, (width, height))

            for image in images:

                image_path = os.path.join(image_folder, image)

                frame = cv2.imread(image_path)
                cv2.putText(frame, str(datetime.now().date()) + "-" + image, (width - 195, height - 30),
                            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, [255, 255, 255],150)
                out.write(frame)  # Write out frame to video

                # # cv2.imshow('video', frame)
                # if (cv2.waitKey(1) & 0xFF) == ord('q'):  # Hit `q` to exit
                #     break

            out.release()

            for image in images:
                image_path = os.path.join(image_folder, image)
                os.remove(image_path)
        except:
            os.mkdir(date_wise_directory)
            pass

        # month=datetime.now().date().strftime("%m")
        # print(month)
        # veh, created = distance_year.objects.get_or_create(vehicle=vehicle)
        # distance= dashboard.objects.get(vehicle_number=vehicle,date=str(datetime.now().date()))
        # if int(month)==1:
        #     print("january")
        #     veh.january=int(veh.january)+int(distance.distance_per_day)
        #     print( veh.january)
        # if int(month)==2:
        #     print("february")
        #     veh.february=int(veh.february)+int(distance.distance_per_day)
        #     print( veh.february)
        # if int(month)==3:
        #     print("march")
        #     veh.march=int(veh.march)+int(distance.distance_per_day)
        #     print( veh.march)
        # if int(month)==4:
        #     print("april")
        #     veh.april=int(veh.april)+int(distance.distance_per_day)
        #     print( veh.april)
        # if int(month)==5:
        #     print("may")
        #     veh.may=int(veh.may)+int(distance.distance_per_day)
        #     print( veh.may)
        # if int(month)==6:
        #     print("june")
        #     veh.june=int(veh.june)+int(distance.distance_per_day)
        #     print( veh.june)
        # if int(month)==7:
        #     print("july")
        #     veh.july=int(veh.july)+int(distance.distance_per_day)
        #     print( veh.july)
        # if int(month)==8:
        #     print("august")
        #     veh.august=int(veh.august)+int(distance.distance_per_day)
        #     print( veh.august)
        # if int(month)==9:
        #     print("september")
        #     veh.september=int(veh.september)+int(distance.distance_per_day)
        #     print( veh.september)
        # if int(month)==10:
        #     print("october")
        #     veh.october=int(veh.october)+int(distance.distance_per_day)
        #     print( veh.october)
        # if int(month)==11:
        #     print("nov")
        #     print(distance.distance_per_day)
        #     veh.november=int(veh.november)+int(distance.distance_per_day)
        #     print( veh.november)
        # if int(month)==12:
        #     print("december")
        #     veh.december=int(veh.december)+int(distance.distance_per_day)
        #     print( veh.december)
        # veh.save()



