from django.shortcuts import render, redirect
from .models import Appointment
from django.shortcuts import HttpResponse

def book_appointment(request):
    appointments = Appointment.objects.all()
    print(appointments)
    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = Appointment(doctor=doctor,date=date,time=time,name=name,email=email,phone=phone,message=message)
        data.save()
        return render(request, 'docdash.html',{"data":appointments})  # Redirect to a success page or any other appropriate URL
    else:
        return HttpResponse("Unsuccessfull")
    
    return render(request,'appointment.html')


