from django.shortcuts import render, redirect
from .models import Appointment
from django.shortcuts import HttpResponse

def book_appointment(request):
    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = Appointment.objects.create(doctor=doctor, date=date, time=time, name=name, email=email, phone=phone, message=message)
        appointments = Appointment.objects.all()  # Query all appointments again after creating the new one
        return render(request, 'docdash.html', {"data": appointments})
    else:
        appointments = Appointment.objects.all()  # Query all appointments if it's not a POST request
        return render(request, 'docdash.html', {"data": appointments})
    
    return render(request, 'appointment.html')
