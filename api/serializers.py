from rest_framework import serializers
from authentication.serializers import UserSerializer
from .models import *


class ProcedureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureType
        fields = '__all__'


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    ptype = ProcedureTypeSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'


