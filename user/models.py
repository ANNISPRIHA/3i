from django.db import models

from datetime import date
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .manager import UserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs=FileSystemStorage(location=settings.MEDIA_ROOT)



user_choices = [
    (None,'type'),
    ('Owner', 'Owner'),
    ('Employee', 'Employee'),
]

class AdminUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=130, unique=True)
    user_type = models.CharField(max_length=10,choices=user_choices,)
    name = models.CharField(_('full name'), max_length=130)
    phone_number = models.BigIntegerField(unique=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    owner_email = models.CharField(max_length=250,null=True)
    name_of_organization = models.CharField(max_length=250,null=True)
    owner_adress = models.CharField(max_length=500,null=True)
    number_of_vehicle = models.IntegerField(null=True)
    number_staff = models.IntegerField(null=True)
    number_driver = models.IntegerField(null=True)
    date_of_joinig = models.DateTimeField(null=True)
    pancard = models.CharField(max_length=20,null=True)
    login=models.BooleanField(default=False)
    owner_photo = models.FileField(storage=fs,null=True,default='download_qf83Viq.jpeg')
    gstnumber = models.CharField(max_length=200,null=True)
    weburl= models.CharField(max_length=200,null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone_number']

    class Meta:
        ordering = ('username',)
        verbose_name = _('Admin User')
        verbose_name_plural = _('Admin Users')

    def get_short_name(self):
        return self.username


class AdminDriver(models.Model):
    owner_name = models.ForeignKey(AdminUser, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=250)
    license_no = models.CharField(max_length=100,null=True)
    hour_on_duty = models.IntegerField(null=True)
    driver_mobile_no = models.CharField(max_length=12,null=True)
    address = models.CharField(max_length=500)
    experience = models.IntegerField(null=True)
    driver_review = models.CharField(max_length=500, null=True)
    driver_photo = models.FileField(storage=fs,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Admin Driver')
        verbose_name_plural = _('Admin Drivers')

class Guest(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone_number = models.BigIntegerField(null=True)
    number_of_vehicle = models.IntegerField(null=True)


    def __str__(self):
        return str(self.phone_number)

class Parent(models.Model):
    parent_name= models.CharField(max_length=100,null=True)
    address= models.TextField(blank=True,null=True)
    parent_phoneno=models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['parent_phoneno']

    def __str__(self):
        return str(self.parent_name)

class child(models.Model):
    child_name= models.CharField(max_length=100,null=True)
    vehical_number=models.CharField(max_length=20,null=True)
    parent=models.ForeignKey(Parent, on_delete=models.SET_NULL,null=True)
    school_name = models.CharField(max_length=8)
    school_arrival_time=models.CharField(max_length=100,null=True)
    school_departure_time=models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.child_name)
