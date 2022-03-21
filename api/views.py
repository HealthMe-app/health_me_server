from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appointment, ProcedureType
from .serializers import AppointmentSerializer


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
        appointments = Appointment.objects.filter(user=self.request.user)
        serializer_class = AppointmentSerializer(appointments, many=True)
        return Response(serializer_class.data)


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

