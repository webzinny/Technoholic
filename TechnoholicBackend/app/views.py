from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Data


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['pas']
        try:
            obj=Data.objects.get(email=email)
            if obj.pas==pas:
                return redirect('course')
            return render(request,'login.html',{'msg':"Wrong Password"})

        except:
            return render(request,'login.html',{'msg':"Email dosen't exists"})
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['pas']
        name=request.POST['name']
        dob=request.POST['yyyy']+"-"+request.POST['mm']+"-"+request.POST['dd']
        gender=request.POST['gender']
        contact=request.POST['contact']
        contact2=request.POST['contact2']
        try:
            obj=Data.objects.get(email=email)
            return render(request,'signup.html',{'msg':'Email already exists'})
        except:
            data=Data(email=email,pas=pas,name=name,dob=dob,gender=gender,contact=contact,contact2=contact2)
            data.save()
            return render(request,'signup.html',{'msg':"Signed Up Successfully, Please proceed to Login"})
    return render(request,'signup.html')

def course(request):
    return render(request,'courseLink.html')
