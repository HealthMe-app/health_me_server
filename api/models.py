from django.contrib.auth import get_user_model
from django.db import models


class TypeBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        abstract = True


class ProcedureType(TypeBase):
    icon = models.ImageField(default='images/doctor.svg')


class Severity(TypeBase):
    icon = models.ImageField(default='images/light.svg')


class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    default_frequency = models.DurationField()
    ptype = models.ForeignKey(ProcedureType, models.DO_NOTHING)


class EntryBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    date_time = models.DateTimeField()
    comment = models.TextField(null=True)
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING)

    class Meta:
        abstract = True


class Appointment(EntryBase):
    address = models.CharField(max_length=255)
    ptype = models.ForeignKey(ProcedureType, models.DO_NOTHING)


class Symptom(EntryBase):
    severity = models.ForeignKey(Severity, models.DO_NOTHING)
