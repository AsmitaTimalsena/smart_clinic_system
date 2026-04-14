from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegisterSerializer
from clinic.models import Doctor


# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        #check for doctor
        if user.role == 'doctor':
            Doctor.objects.create(user=user, name=user.username)


        return Response('Registration Successful')
    return Response(serializer.errors)