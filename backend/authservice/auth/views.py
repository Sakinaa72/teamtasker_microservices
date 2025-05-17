import jwt 
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        email=request.data.get('email')
        password=request.data.get('password')
        user= authenticate(username=email, password=password)
        if user:
            payload = {'user_id':user.id, 'email':user.email}
            token=jwt.encode(payload, 'your_secret_key', algorithm='HS256')
            return Response({'token':token}, status=status.HTTP_200_OK)
        return Response({'error':'Invalid credentials'}, status=)

class RegisterView(APIView):
    pass 

