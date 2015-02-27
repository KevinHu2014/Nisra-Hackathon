from django.shortcuts import render
<<<<<<< HEAD
from models import User
from models import Message
from models import Send
=======
# git test
>>>>>>> 6af46303fc0b315c87989838b0f5159ffe9255fe
# Create your views here.
def checkLogin(request):
    email = request.POST["email"]
    password = request.POST["password"]

    User.objects.filter(Q(userEmail=email)&Q(userPassword=password)).count()
    return HttpResponse(data)
