from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import department,courses
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if  request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'new.html')
        else:
            messages.info(request,"Invalid login")
            return redirect('schoolApp:login')


    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['psw']
        cpassword=request.POST['psw-repeat']
        if password==cpassword:
            if User.objects.filter(username=username).exists():

                messages.info(request,"User name already exists")
                return redirect('schoolApp:register')
                #print(request,"user error")

            else:

                 user=User.objects.create_user(username=username, password=password)
                 user.save();
                 return redirect('schoolApp:login')
                 #messages.info(request,"user created")
        else:

            messages.info(request,"Incorrect password")
            return redirect('schoolApp:register')
        return redirect('/')
    return render(request,'register.html')

def demo(request):
    obj=department.objects.all()
    return render(request,'department.html',{'links':obj})

def logout(request):
    auth.logout(request)
    return redirect('/')
def logoutf(request):
    return render(request,'department.html')

def newForm(request):
    obj=department.objects.all()
    obj1=courses.objects.all()
    return render(request,'newForm.html',{'links':obj,'links1':obj1})


def confirm(request):
    return render(request,'confirm.html')