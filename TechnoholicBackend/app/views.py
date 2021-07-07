from django.shortcuts import render
from django.http import HttpResponse
from .models import Data


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['pas']
        name=request.POST['name']
        dob=request.POST['name']
        gender=request.POST['gender']
        contact=request.POST['contact']
        contact2=request.POST['contact2']
        print("[The DATA is]",end="->")
        print(email,pas,name,dob,gender,contact,contact2)
        data=Data(email=email,pas=pas,name=name,dob=dob,gender=gender,contact=contact,contact2=contact2)
        # data.save()
    return render(request,'signup.html')

def course(request):
    return render(request,'courseLink.html')
