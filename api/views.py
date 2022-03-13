import logging

from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from django.http.response import JsonResponse

from authentication.serializers import UserSerializer
from authentication.views import UserAPI
from .models import ProcedureType, Procedure, Appointment
from .serializers import ProcedureTypeSerializer, ProcedureSerializer, AppointmentSerializer
from authentication.models import User


@csrf_exempt
def appointmentAPI(request, id=0):

    if request.method == 'GET':
        appointments = Appointment.objects.all()
        appointments_serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(appointments_serializer.data, safe=False)

    if request.method == 'POST':
        appointment_data = JSONParser().parse(request)
        appointments_serializer = AppointmentSerializer(data=appointment_data)
        if appointments_serializer.is_valid():
            appointments_serializer.save()
            return JsonResponse("Запись успешно добавлена", safe=False)
        return JsonResponse("{}".format(get_user(request)), safe=False)

    if request.method == 'PUT':
        appointment_data = JSONParser().parse(request)
        appointment = Appointment.objects.get(id=appointment_data['id'])
        appointments_serializer = AppointmentSerializer(appointment, data=appointment_data)
        if appointments_serializer.is_valid():
            appointments_serializer.save()
            return JsonResponse("Запись успешно отредактирована", safe=False)
        return JsonResponse("Ошибка редактирования записи", safe=False)

    if request.method == 'DELETE':
        appointment = Appointment.objects.get(id=id)
        appointment.delete()
        return JsonResponse("Запись успешно удалена", safe=False)
