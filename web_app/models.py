from django.db import models

# Create your models here.

class LoginDetails(models.Model):
    username = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.username

    
    empAuth_objects = models.Manager()
