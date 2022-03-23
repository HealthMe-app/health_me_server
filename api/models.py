from django.contrib.auth import get_user_model
from django.db import models


class ProcedureType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    icon = models.ImageField(default='images/doctor.svg')


class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    default_frequency = models.DurationField()
    ptype = models.ForeignKey(ProcedureType, models.DO_NOTHING)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    comment = models.TextField(null=True)
    ptype = models.ForeignKey(ProcedureType, models.DO_NOTHING)
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING)
