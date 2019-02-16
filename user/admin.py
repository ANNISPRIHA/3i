from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import *


class DriverAdmin(admin.ModelAdmin):
    search_fields = ['name']

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']

admin.site.register(AdminDriver,DriverAdmin)
admin.site.register(AdminUser,UserAdmin)

