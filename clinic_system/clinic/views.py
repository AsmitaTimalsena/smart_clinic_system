from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer


@api_view(['GET','POST'])
def doctor_list(request):
    if request.method == "GET":
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, pk):
   try:
      doctor = Doctor.objects.get(pk=pk)
   except Doctor.DoesNotExist:
      return Response({"error : Not Found"}, status=status.HTTP_404_NOT_FOUND)
   if request.method == 'GET':
      serializer = DoctorSerializer(doctor)
      return Response(serializer.data)
   if request.method == 'PUT':
      serializer = DoctorSerializer(doctor, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   if request.method == 'DELETE':
      doctor.delete()
      return Response({"message": "deleted"})

@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    except Patient.DoesNotExist:
        return Response({"error : Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "DELETE":
        patient.delete()
        return Response({"message": "deleted"})

@api_view(['GET', 'POST'])
def appointment_list(request, pk):
    if request.method == "GET":
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    except Appointment.DoesNotExist:
        return Response({"error : Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    if request.method == "DELETE":
        appointment.delete()
        return Response({"message": "deleted"})


