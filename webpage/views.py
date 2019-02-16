from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from django.contrib.sites import requests
from django_otp.oath import totp
from django.shortcuts import render, Http404, HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
import http.client
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import os



from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.contrib.sites import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render,redirect
import json
from user.models import *
from track.models import *


def Index_View(request):
    return render(request,'index.html')


@csrf_exempt
#purpose::its can use for login with authentication
def Login_View(request):
        try:
                response_data = {}
                username = request.GET['username']
                password = request.GET['password']
                request.session['username'] = username
                request.session['time'] = str(datetime.now().minute)
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                        response_data['status'] = "success"
                        return HttpResponse(json.dumps(response_data), content_type="application/json")
                else:
                    # messages.warnning(request,'Incorrect Credential',fail_silently=True)
                    response_data['status'] = "Please ! Enter valid usename, password"
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
        except:
            logout(request)
            return redirect('/login')


def Home_View(request):

     return render(request,'home.html',{'user':request.session['username']})

def VehicleShow(request):
     request.session['carS'] = request.GET['car']
     return HttpResponse(json.dumps("success"), content_type="application/json")



def carView(request):
    return render(request, 'vehicle.html', {'carS': request.session['carS']})


def route(request):
    owner=AdminUser.objects.get(username=request.session['username'])
    cars=Vehicle.objects.filter(owner=owner)
    return render(request,'route.html',{'cars':cars})