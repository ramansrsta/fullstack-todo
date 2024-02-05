from .models import Student
from .serializers import StudentSerializer
from .throttling import UpdatedRateThrottle

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UpdatedRateThrottle, AnonRateThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields=['^name']
    ordering_fields=['name']
    ordering = ['-city']


    





 

