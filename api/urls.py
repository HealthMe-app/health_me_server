from django.urls import path
from api import views

urlpatterns = [
    path('appointment/', views.AppointmentView.as_view()),
    path('appointments', views.UserAppointmentView.as_view()),
    path('appointment/<int:pk>', views.AppointmentDetailView.as_view()),
    path('symptom/', views.SymptomView.as_view()),
    path('symptoms', views.UserSymptomView.as_view()),
    path('symptom/<int:pk>', views.SymptomDetailView.as_view())
]
