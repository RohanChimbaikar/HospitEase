from django.http import HttpResponse
from django.shortcuts import render 
from appointment.models import Appointment
def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,"home.html")

def facility(request):
    return render(request,"facility.html")

def login(request):
    return render(request,"templates/Login.html")

def registration(request):
    return render(request,"templates/registration.html")

def feed(request):
    return render(request,"templates/feed.html")

def vac(request):
    return render(request,"templates/vac.html")

def xray(request):
    return render(request,"templates/xray.html")

def physio(request):
    return render(request,"templates/physio.html")

def sono(request):
    return render(request,"templates/sono.html")

def log(request):
    
    return render(request,"templates/Loginint.html")

def logg(request):
    return render(request,"templates/Login_inst.html")

def appoint(request):
    return render(request,"appointment.html")

def dash(request):
    return render(request,"templates/admindash.html")

