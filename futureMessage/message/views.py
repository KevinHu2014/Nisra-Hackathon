from django.shortcuts import render
from models import User
from models import Message
from models import Send
# Create your views here.
def checkLogin(request):
    email = request.POST["email"]
    password = request.POST["password"]

    User.objects.filter(Q(userEmail=email)&Q(userPassword=password)).count()
    return HttpResponse(data)
