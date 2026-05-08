from django.core.serializers import deserialize
from rest_framework import serializers
from .models import Doctor, Patient, Appointment


class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
       model = Doctor
       fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    patient = serializers.StringRelatedField()
    class Meta:
        model = Appointment
        fields = '__all__'