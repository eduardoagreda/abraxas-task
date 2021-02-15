from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    def __str__(self):
        return '%s %s - %s' %(self.first_name, self.last_name, self.username)

