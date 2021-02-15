from django.db import models

class BaseModel(models.Model):
    """ Base model from all models to implements in this project. """
    created_at = models.DateTimeField('Date and time of object created', auto_now_add=True)
    updated_at = models.DateTimeField('Date and time of object updated', auto_now=True)

    class Meta:
        abstract = True

