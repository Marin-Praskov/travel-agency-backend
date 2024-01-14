from django.contrib import admin
from .models import Location, Holiday, Reservation

# Register your models here.
admin.site.register(Location)
admin.site.register(Holiday)
admin.site.register(Reservation)