# Django 
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model


# rest framework
from rest_framework import status

# Models
from apps.task.models import Task

# Serializer
from apps.task.serializers import TaskModelSerializer

# Json
import json


TASK_URL = reverse('task-list')

class TaskApiTest(TestCase):
   
    def setUp(self):
        """
           Creation of user for tests.
        """
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            'eduardo@truehome.mx',
            'holatruehome'
        )
        self.client.force_login(self.user)

        self.task_one = Task.objects.create(description='Task 1', status=1, duration=45)
        self.task_two = Task.objects.create(description='Task 2', status=2, duration=90, total_time='01:15:00')

        self.payload_task_complete = {
            'description': 'Task 1',
            'status': 2,
            'duration': 90,
            'total_time': '01:30:00'
        }

        self.payload_task_pending = {
            'description': 'Task 2',
            'status': 1,
            'duration': 60,
            'total_time': '00:45:00'
        }
    
    def test_retrive_tasks_list(self):
        Task.objects.create(description='Test 1', status=1, duration=45, total_time='00:35:00')
        Task.objects.create(description='Test 2', status=2, duration=90, total_time='01:30:00')

        response = self.client.get(TASK_URL)
        tasks       = Task.objects.all()
        serializer  = TaskModelSerializer(tasks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tasks(self):
        """
            Function of create task.
        """
        payload_pending = {
            'description': 'Test 1', 
            'status': 1, 
            'duration': 30
        }

        payload_complete = {
            'description': 'Test 2',
            'status': 2,
            'duration': 60,
            'total_time': '00:45:00'
        }

        response_task_pending  = self.client.post(TASK_URL, data=json.dumps(payload_pending), content_type='application/json')
        response_task_complete = self.client.post(TASK_URL, data=json.dumps(payload_complete), content_type='application/json')

        self.assertEqual(response_task_pending.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_task_complete.status_code, status.HTTP_201_CREATED)

        """
            Checking if pending task has found in database
        """
        exist_pending = Task.objects.filter(
            description = payload_pending['description'],
            status=1
        ).exists()
        self.assertTrue(exist_pending)

        """
            Checking if complete task has found in database
        """
        exist_complete = Task.objects.filter(
            description = payload_complete['description'],
            status=2
        ).exists()
        self.assertTrue(exist_complete)

    def test_retrive_task(self):
        response   = self.client.get(reverse('task-detail', kwargs={'pk': self.task_one.pk}))
        task_one   = Task.objects.get(pk=self.task_one.pk)
        serializer = TaskModelSerializer(task_one)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_fail_task(self):
        response   = self.client.put(
            reverse('task-detail', kwargs={'pk': self.task_two.pk}),
            data=json.dumps(self.payload_task_pending),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_304_NOT_MODIFIED)

    def test_update_task(self):
        response = self.client.put(
            reverse('task-detail', kwargs={'pk': self.task_one.pk}),
            data=json.dumps(self.payload_task_complete),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_task(self):

        partial_update = {'total_time': '00:30:00'}

        response = self.client.patch(
            reverse('task-detail', kwargs={'pk': self.task_one.pk}),
            data=json.dumps(partial_update),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(
            reverse('task-detail', kwargs={'pk': self.task_one.pk}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        """
            Checking if task one has been deleted of database
        """

        response = self.client.delete(
            reverse('task-detail', kwargs={'pk': self.task_one.pk}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)