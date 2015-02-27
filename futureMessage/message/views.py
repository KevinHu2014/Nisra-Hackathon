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
# git test
# Create your views here.
@csrf_exempt
def checkLogin(request):
    print request.POST
    email = request.POST["email"]
    password = request.POST["password"]
    success = User.;objects.filter(Q(userEmail=email)&Q(userPassword=password)).count()
    if success == 0:
	
    else
	
    return HttpResponse(data)

def loginPage(request):
    return render_to_response('Login.html')
    
