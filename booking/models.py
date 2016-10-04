from __future__ import unicode_literals

from django.contrib.auth.models import User, AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class VehicleInformation(models.Model):
    FIRST_CHOICE = 0
    SECOND_CHOICE = 1
    VEHICLE_TYPE_CHOICES = (
        (FIRST_CHOICE, 'Two Wheeler'),
        (SECOND_CHOICE, 'Four Wheeler')
    )
    IS_VERIFIED_CHOICES = (
        (FIRST_CHOICE, 'No'),
        (SECOND_CHOICE, 'Yes')
    )
    vehicle_type = models.CharField(max_length=50, null=False, blank=False, choices=VEHICLE_TYPE_CHOICES)
    vehicle_reg_no = models.CharField(null=False, blank=False, max_length=50)
    is_verified = models.SmallIntegerField(null=False, blank=False, choices=IS_VERIFIED_CHOICES)

    def __unicode__(self):
        return "{} - {}".format(self.id, self.vehicle_reg_no)


class Person(AbstractBaseUser):
    email = models.EmailField(_('Email Address'), unique=True, db_index=True, null=False, blank=False)
    first_name = models.CharField(null=False, blank=False, max_length=20)
    last_name = models.CharField(null=False, blank=False, max_length=20)
    dob = models.DateField(null=True, blank=True)
    contact_number = models.CharField(_("Mobile Number"), max_length=20)
    vehicle_info = models.ForeignKey(VehicleInformation, null=True, blank=True)

    def __unicode__(self):
        return "{} - {}".format(self.id, self.email)
