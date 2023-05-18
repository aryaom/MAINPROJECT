from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class addgroup(models.Model):
    groups=models.CharField(max_length=20)

class groupadmins(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    mailid=models.CharField(max_length=20)
    phonenum=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    group=models.CharField(max_length=20)

class pattern(models.Model):
    patternname=models.CharField(max_length=20)

class p1_tb(models.Model):
    v1=models.CharField(max_length=20)

class expectedchisquare_tb(models.Model):
    expected_chi_value=models.CharField(max_length=20)
    groupname=models.CharField(max_length=20)
