from django.shortcuts import render_to_response
from models import User
from models import Message
from models import Send
from time import strftime
# git test
# Create your views here.
def checkLogin(request):
    email = request.POST["email"]
    password = request.POST["password"]
    success = User.objects.filter(Q(userEmail=email)&Q(userPassword=password)).count()
    if success == 0:
        data = 'Login Error'
    else:
        data = 'Login Success'
    return HttpResponse(data)
def loginPage(request):
    return render_to_response('Login.html')
    
