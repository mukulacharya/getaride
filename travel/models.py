__author__ = 'mukul'

from django.db import models
from django.contrib.gis.db import models as geo_models
import datetime
from booking.models import VehicleInformation, Person


class TravelInformation(geo_models.Model):
    source_location = geo_models.PointField(null=True, blank=True, editable=False)
    destination_location = geo_models.PointField(null=True, blank=True, editable=False)
    current_location = geo_models.PointField(null=True, blank=True, editable=False)
    travel_distance = geo_models.DecimalField(default=0, blank=False, null=False, decimal_places=2, max_digits=8)
    vehicle_information = geo_models.ForeignKey(VehicleInformation, null=False, blank=False)
    date = geo_models.DateField(default=datetime.date.today)
    start_time = geo_models.DateTimeField(default=datetime.datetime.now())
    end_time = geo_models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return "{} - {}".format(self.id, self.vehicle_information)


class RiderInfo(models.Model):
    rider = models.ForeignKey(Person, null=False, blank=False, related_name="rider_person")
    pillion_rider = models.ForeignKey(Person, null=True, blank=True, related_name="pillionrider_person")
    rider_travel_info = models.ForeignKey(TravelInformation, null=True, blank=True, related_name="rider_travelinfo")
    pillion_rider_travel_info = models.ForeignKey(TravelInformation, null=True, blank=True,
                                                  related_name="pillionrider_travelinfo")

    def __unicode__(self):
        return "{} - {}".format(self.rider, self.pillion_rider)