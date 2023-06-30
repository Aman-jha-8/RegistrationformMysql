from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Registration,Regg
import re

def reg(req):
    return render(req,'registration.html')

def suc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        college = request.POST.get('college')
        dob = request.POST.get('dob')
        # emailRegex = re.compile("/ ^ [ ^\s@]+ @ [ ^\s@]+\.[ ^\s @]+$ /")
        # passwordRegex = re.compile("/ ^ (?=.*[A-Z])(?=.* \d).{8, }$ /")
        # if emailRegex.match(email) and passwordRegex.match(password):
        registration = Registration(name=name, phone=phone, email=email, address=address, password=password, confirmPassword=confirmPassword, college=college, dob=dob)
        registration.save()
        return render(request,'suc.html')
        # else:
        #     return HttpResponse('please enter correct mail and pswd')
    else:
        return HttpResponse('error use get')

def qoute(req):
    return render(req,"qoute.html")

def hom(req):
    return render(req,'regg.html')

def homsuc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender=request.POST.get('gender')
        college = request.POST.get('college')
        regist = Regg(name=name,email=email,password=password,gender=gender,college=college)
        regist.save()
        return render(request,'suc.html')
    else:
        return HttpResponse('sent with post not get')

def all(req):
    return render(req,'Allconnect.html')