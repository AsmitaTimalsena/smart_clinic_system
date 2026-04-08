from rest_framework.routers import DefaultRouter

from django.urls import path
from .views import doctor_list, doctor_detail, patient_list, patient_detail,appointment_list, appointment_detail

urlpatterns = [
    path('doctors/',doctor_list),
    path('doctors/<int:pk>/',doctor_detail),
    path('patients/', patient_list),
    path('patients/<int:pk>/', patient_detail),
    path('appointments/', appointment_list),
    path('appointments/<int:pk>/', appointment_detail)
]
