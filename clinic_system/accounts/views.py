from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import RegisterSerializer
from clinic.models import Doctor, Patient
from .models import User
from .models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        # check for doctor or patient
        if user.role == "doctor":
            Doctor.objects.create(user=user)

        elif user.role == "patient":
            Patient.objects.create(user=user)
        print("Doctor count:", Doctor.objects.count())
        print("Patient count:", Patient.objects.count())
        return Response({"message": "Registration successful"})
    else:
        print("ERRORS:", serializer.errors)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({
        'username': request.user.username,
        'role': request.user.role,
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_list(request):
    users = User.objects.all().values('id', 'username', 'role')
    return Response(list(users))