from django.shortcuts import render
from rest_framework import generics, views, response, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import RegisterSerializer, EmailTokenObtainPairSerializer, UserInfoSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class GetUserInfoView(APIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserInfoSerializer(request.user)
        return Response(serializer.data)


class GetPeopleInfoView(APIView):
    serializer_class = UserInfoSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data)