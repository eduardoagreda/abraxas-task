# Serializer
from apps.task.serializers import TaskModelSerializer

# Rest Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# filters
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

# Parsers
from rest_framework.parsers import JSONParser
from rest_framework_xml.parsers import XMLParser

# Pagination
from apps.task.pagination import CustomPagination

# Renders
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_xml.renderers import XMLRenderer

# Models
from apps.task.models import Task

# django
from django.shortcuts import get_object_or_404

# Json
import json

# Settings
from tareas.settings import BASE_DIR

# Create your views here.

class TaskViewSet(ModelViewSet):
    """
        CRUD from task model, include search of task
    """
    queryset            = Task.objects.all()
    serializer_class    = TaskModelSerializer
    renderer_classes    = (JSONRenderer, XMLRenderer, BrowsableAPIRenderer,)
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['status',]
    pagination_class    = (CustomPagination)

    def retrive(self, request, pk=None):       
        queryset    = Task.objects.all()
        task        = get_object_or_404(queryset, pk=pk)

        serializer  = TaskModelSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            queryset    = Task.objects.all()
            task        = get_object_or_404(queryset, pk=pk)
            if task.status == 2:
                message = "Can't update this task"
            else:
                serializer = TaskModelSerializer(task, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    message = 'An error occurred'
            return Response({'data': message}, status=status.HTTP_304_NOT_MODIFIED)
        except Exception as ex:
            print(ex)
            pass
    
    def partial_update(self, request, pk=None):
        try:
            queryset    = Task.objects.all()
            task        = get_object_or_404(queryset, pk=pk)
            if task.status == 2:
                message = "Can't update this task"
            else:
                serializer = TaskModelSerializer(task, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    message = 'An error occurred'
            return Response({'data': message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            pass

    def destroy(self, request, pk=None):
        queryset        = Task.objects.all()
        task            = get_object_or_404(queryset, pk=pk)
        if task:
            task.delete()
            message = 'Task deleted'
            return Response({'data': message}, status=status.HTTP_200_OK)
        else:
            message = "Not data found"
            return Response({'data': message}, status=status.HTTP_404_NOT_FOUND)
        
class TaskListView(ListAPIView):
    queryset            = Task.objects.all()
    serializer_class    = TaskModelSerializer
    renderer_classes    = (JSONRenderer, XMLRenderer, BrowsableAPIRenderer,)
    filter_backends     = [SearchFilter, OrderingFilter]
    search_fields       = ['description', 'duration',]
    ordering_fields     = ['status', 'duration',]

class TaskBulkAPIView(APIView):
    """
        Class based viewd for add bulk tasks with json file.
    """
    def post(self, request):
        with open(str(BASE_DIR)  + '/tasks.json', 'r') as f:
            task_dict = json.load(f)

        for task in task_dict:
            create_task = Task.objects.create(
                description=task['description'], 
                status=task['status'], 
                duration=task['duration'],
                total_time=task['total_time'])
        message = 'Add tasks'
        return Response({'message': message, 'data': task_dict})