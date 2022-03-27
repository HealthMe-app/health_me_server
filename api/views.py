from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appointment, ProcedureType, Severity, Symptom
from .serializers import AppointmentSerializer, SymptomSerializer


class AppointmentView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        ptype = generics.get_object_or_404(ProcedureType, id=self.request.data.get('ptype'))
        return serializer.save(user=user, ptype=ptype)


class UserAppointmentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        appointments = Appointment.objects.filter(user=self.request.user,
                                                  date_time__gte=timezone.localtime()).order_by('date_time')[:2]
        serializer_class = AppointmentSerializer(appointments, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        if not self.request.data.get('date'):
            raise ValueError("Выберите дату")
        appointments = Appointment.objects.filter(user=self.request.user,
                                                  date_time__date=self.request.data.get('date')).order_by('date_time')
        serializer_class = AppointmentSerializer(appointments, many=True)
        return Response(serializer_class.data)


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class SymptomView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    def perform_create(self, serializer):
        user = self.request.user
        severity = generics.get_object_or_404(Severity, id=self.request.data.get('severity'))
        return serializer.save(user=user, severity=severity)


class UserSymptomView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if not self.request.data.get('date'):
            raise ValueError("Выберите дату")
        symptoms = Symptom.objects.filter(user=self.request.user,
                                          date_time__date=self.request.data.get('date')).order_by('date_time')
        serializer_class = SymptomSerializer(symptoms, many=True)
        return Response(serializer_class.data)


class SymptomDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
