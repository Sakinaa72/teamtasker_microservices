from django.shortcuts import render
from django.contrib.auth import authenticate
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(username=email, password=password) 
        if user:
            payload={'user_id':user.id, 'email':user.email}
            token=jwt.encode(payload, 'your_secret_key', algorithm='HS256')
            return Response({'token':token}, status=status.HTTP_200_OK)
        return Response({'error':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

class RegisterView(APIView):
    def post(self, request):
        email=request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            return Response({'error':'Email and password are required'}, status=status.HTTP_404_NOT_FOUND)
        user=User.objects.create_user(username=email, password=password)
        return Response({'message':'User created'}, status=status.HTTP_201_CREATED)
     
