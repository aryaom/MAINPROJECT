from django.db import models
from SiteAdmin.models import *

# Create your models here.
class mentorsregistration(models.Model):
    mentorname=models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    emailid = models.CharField(max_length=20)
    phoneno = models.CharField(max_length=20)
    qualification = models.CharField(max_length=20)
    experience = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    grpadmin_id = models.ForeignKey(groupadmins,on_delete=models.CASCADE)
    status = models.CharField(max_length=20)


