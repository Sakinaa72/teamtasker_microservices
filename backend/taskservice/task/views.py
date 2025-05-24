from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class TaskView(APIView):
    def post(self, request):
        data=request.data.copy()
        data['created_by']=request.user_info['user_id']
        serializer=TaskSerializer(data=data)
        if serializer.is_valid():
            task=serializer.save()
            return Response({'message':"Task created",'task_id':task.id}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, task_id=None):
        if task_id:
            task=Task.objects.filter(id=task_id).first()
            if not task:
                return Response({'error':"Task not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer=TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        tasks=Task.objects.all()
        seralizer=TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, task_id):
        task=Task.objects.filter(id=task_id).first()
        if not task:
            return Response({'error':"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Task updated"}, staus=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, task_id):
        task=Task.objects.filter(id=task_id).first()
        if not task:
            return Response({'error':"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response({'message':"Task deleted"}, status=status.HTTP_204_NO_CONTENT)
        