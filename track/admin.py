from django.contrib import admin
from .models import*
# Register your models here.

class AAdmin(admin.ModelAdmin):
    search_fields = ['vehicle_number']


admin.site.register(Location,AAdmin)

admin.site.register(Vehicle,AAdmin)
admin.site.register(image_vehicle,AAdmin)