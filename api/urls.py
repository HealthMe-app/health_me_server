from django.urls import re_path, path
from api import views

urlpatterns = [
    path('appointment', views.appointmentAPI),
    path('appointment/', views.appointmentAPI),
    re_path(r'^appointment/([0-9]+)$', views.appointmentAPI)
]
