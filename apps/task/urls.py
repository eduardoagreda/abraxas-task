from django.urls import path, include 

# Views
from apps.task.views import TaskViewSet
from apps.task.views import TaskListView
from apps.task.views import TaskBulkAPIView

task_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

task_detail = TaskViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

task_search = TaskListView.as_view()

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('task/<int:pk>/', task_detail, name='task-detail'),
    path('tasks/search/', task_search, name = 'task-seach'),
    path('tasks/insert/', TaskBulkAPIView.as_view(), name = 'insert-bulk-tasks'),
]
