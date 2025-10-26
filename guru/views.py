from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("it is an first app it is prajwal")

def demo(request):
    return HttpResponse("it is an second home page")