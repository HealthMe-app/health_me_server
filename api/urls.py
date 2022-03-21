from django.urls import path
from api import views

urlpatterns = [
    path('appointment/', views.AppointmentView.as_view()),
    path('appointments', views.UserAppointmentView.as_view()),
    path('appointment/<int:pk>', views.AppointmentDetailView.as_view())
]
