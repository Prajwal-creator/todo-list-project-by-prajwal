from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import User
from .models import log 
import random
from datetime import datetime
from django.contrib import messages

def loging(request):
    if request.method=="POST":
        name=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=name,password=passw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"username or password is incarrect")
    return render(request,'loginn.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        k=User.objects.create_user(username=username,email=email,password=password)
        k.save()
        return redirect('dock')
    return render(request,'signup.html')

def amd(request,srno):
    print(srno)
    if request.method=="POST":
        new_task=request.POST.get("taskDescription")
        print(new_task)
        user=request.user
        old=log.objects.get(srno=srno)
        old.username=new_task
        old.save()
        return redirect('home')
    return render(request,'edit.html')

def home(request):
    user=request.user
    if request.method=='POST':
        text=request.POST.get("toodo")
        print(text)
        out=log.objects.create(username=text,user=user)
        out.save()
    user=request.user
    eng=log.objects.filter(user=user).order_by('-ryzen')
    num_obj=log.objects.filter(user=user).count()
    return render(request,'home.html',{'name':user,'eng':eng,'num_obj':num_obj})

def delete_task(request,srno):
    print(srno)
    task = log.objects.get(srno=srno)
    task.delete()
    return redirect('home')
