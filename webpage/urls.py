from django.conf.urls import url
from django.contrib import admin

from webpage import views
app_name = 'website'
urlpatterns = [
    url(r'^$', views.Index_View),
    url(r'^login/$', views.Login_View, name='Login_View'),
    url(r'^home/$', views.Home_View ),
    url(r'^VehicleShow/$', views.VehicleShow),
    url(r'^carView/$', views.carView),
    url(r'^route/$', views.route),
    ]