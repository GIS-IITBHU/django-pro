from django.contrib import admin
from .models import Hostels, Incidences
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    list_display =("name","location")

class HostelsAdmin(LeafletGeoAdmin):
    list_display =("name","country","hostelid")



admin.site.register(Incidences,IncidencesAdmin)
admin.site.register(Hostels,HostelsAdmin)
