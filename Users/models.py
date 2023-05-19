from django.db import models

from Mentors.models import *
from GroupAdmin.models import *
# Create your models here.


class userregistration_tb(models.Model) :
    fname=models.CharField(max_length=20,default="hh")
    lastname = models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    pincode=models.CharField(max_length=20,default="nothing")
    mailid=models.CharField(max_length=20)
    phonenum=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    experience = models.CharField(max_length=20,default="nothing")
    designation = models.CharField(max_length=20,default="nothing")
    companyname = models.CharField(max_length=20,default="nothing")
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class addqueryUSER_tb(models.Model) :
    subject=models.CharField(max_length=30,default="spam")
    addquery=models.CharField(max_length=220,default="spam")
    fileupload=models.FileField()
    group=models.CharField(max_length=20,default="spam")
    user_id = models.ForeignKey(userregistration_tb, on_delete=models.CASCADE)
    date=models.CharField(max_length=20,default="spam")
    status=models.CharField(max_length=20,default="pending")
    status_post=models.CharField(max_length=20,default="Valid")
    status_file=models.CharField(max_length=20,default="Valid")


class usercomplaints_tb(models.Model) :
    mentor_id= models.ForeignKey(mentorsregistration, on_delete=models.CASCADE)
    user_id = models.ForeignKey(userregistration_tb, on_delete=models.CASCADE)
    about=models.CharField(max_length=20,default="nothing")
    details=models.CharField(max_length=20,default="nothing")
    date=models.CharField(max_length=20,default="nothing")
#mentors
class reply_mentor(models.Model):
    query_id=models.ForeignKey(addqueryUSER_tb,on_delete=models.CASCADE)
    mentor_id=models.ForeignKey(mentorsregistration,on_delete=models.CASCADE)
    reply=models.CharField(max_length=20)
    fileupload=models.FileField()
    date=models.CharField(max_length=20)
    status_post=models.CharField(max_length=20)
    status_file=models.CharField(max_length=20)


#GroupAdmins
class QueryAllocation(models.Model):
    mentorid = models.ForeignKey(mentorsregistration,on_delete=models.CASCADE)
    queryid=models.ForeignKey(addqueryUSER_tb,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
