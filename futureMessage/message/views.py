#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import User
from models import Message
from models import Send
from time import strftime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db import connection
import random
# git test
# Create your views here.
@csrf_exempt
def checkLogin(request):
    if request.method == 'GET':
	    res = HttpResponse()
		res.write('sdgsdfg')
		return res
	else:
        print request.POST
        email = request.POST.get("email")
        password = request.POST.get("password")
        success = User.objects.filter(Q(userEmail=email)&Q(userPassword=password)).count()
        if success == 0:
           return render_to_response('future/fail.html')
        else:
           return render_to_response('future/success.html')    
def checkLogin2(request)
    res = HttpResponse()
    res.write('sdgsdfg')
    return res
def loginPage(request):
    return render_to_response('Login.html')
  
def userAdd(request):
    name = request.POST["userName"]
    email = request.POST["userEmail"]
    password = request.POST["password"]
    checkCode = random.randint(1000,10000)
    while User.objects.filter(checkCode=checkCode).count() > 0:
        checkCode = random.randint(1000,10000)
    success = User.objects.filter(userEmail=email).count()
    if success == 0:
        user = User(userName=name,userEmail=email,userPassword=password,checkCode=checkCode)
        user.save()
        checkLink = 'https://128.199.247.129:8080/vertifyCheckCode?verifyID={0}'.format(checkCode)
        mail_title = 'Verify Mail'
        message    = 'Your Link is {0}'.format(checkLink)
        email = settings.DEFAULT_FROM_EMAIL
        recipients = email.split(',')
        sysTime = strftime('%Y%m%d%H%M')
        mailNumber = User.objects.filter(endTime=sysTime)
        while mailNumber > 0:
            send_mail(mail_title,message,email,recipients,settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        return render_to_response('future/UserSuccess.html')
    else:
        return render_to_response('future/UserFail.html')
        
def verifyCheckCode(request):
    check = request.GET["checkCode"]
    vertigyCheck = User.objects.filter(checkCode=check).count()
    if vertigyCheck == 0:
        return render_to_response('future/UserSuccess.html')
    else:
        vertigyCheck = User.objects.get(checkCode=check)
        vertigyCheck.inVaild = True
        return render_to_response('future/UserSuccess.html')
def pageReg(request):
    return render_to_response('future/Registration.html')
    