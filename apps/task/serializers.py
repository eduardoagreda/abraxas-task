# Serializer
from rest_framework.serializers import ModelSerializer

# Models
from apps.task.models import Task

class TaskModelSerializer(ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.date_task   = validated_data.get('date_task', instance.date_task)
        instance.duration    = validated_data.get('duration', instance.duration)
        instance.status      = validated_data.get('status', instance.status)
        instance.total_time  = validated_data.get('total_time', instance.total_time)
        instance.save()
        return instance