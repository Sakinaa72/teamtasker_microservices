from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.

class ProfileView(APIView):
    def get(self, request, user_id):
        profile=Profile.objects.filter(user_id=user_id).first()
        if not profile:
            return Response({"error":"Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, user_id):
        profile, created=Profile.objects.get_or_create(user_id=user_id)
        serialiazer=ProfileSerializer(profile, data=request.data, partial=True)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'message':"Profile updated"}, status=status.HTTP_201_CREATED)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)