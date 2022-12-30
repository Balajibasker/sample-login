from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class login_data(models.Model):
    username=models.CharField(max_length=20,default="")
    password = models.CharField(max_length=20,default="")
    
    #Contact=models.IntegerField(default="")
    email=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.username