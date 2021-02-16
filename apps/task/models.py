from django.db import models

from apps.utils.models import BaseModel

# Create your models here.

class Task(BaseModel):
    """ Task model extends of Base Model. """
    DURATION_CHOICE = [
        (15, '15 minutes'),
        (30, '30 minutes'),
        (45, '45 minutes'),
        (60, '60 minutes'),
        (75, '75 minutes'),
        (90, '90 minutes')
    ]

    STATUS_CHOICE = [
        (1, 'Pendiente'),
        (2, 'Completado')
    ]

    description = models.TextField('Field from task name', blank=True, null=True)
    date        = models.DateField("User's task assignation date", blank=True, null=True)
    duration    = models.IntegerField('Task time life in minutes', choices=DURATION_CHOICE)
    status      = models.IntegerField('Status task', choices=STATUS_CHOICE, default=1)
    total_time  = models.TimeField("Users' time of task finish", blank=True, null=True)

    def get_status(self):
        return self.status

    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ['status']