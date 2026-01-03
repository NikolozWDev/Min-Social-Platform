from django.shortcuts import render
from rest_framework import generics, views, response, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import RegisterSerializer, EmailTokenObtainPairSerializer

# Create your views here.
