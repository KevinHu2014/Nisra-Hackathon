from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userEmail = models.CharField(max_length=30,unique=True)
    userPassword = models.CharField(max_length=30)
    inVaild = models.BooleanField(default=False)
    checkCode = models.CharField(max_length=10)
class Message(models.Model):
    messageID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    endTime = models.CharField(max_length=12)
class Send(models.Model):
    mid = models.ForeignKey('Message')
    uid = models.Foreignkey('User')