from django.shortcuts import render, redirect
from .models import Appointment
from django.shortcuts import HttpResponse
from django.http import *
from django.core.mail import send_mail
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


def send_acceptance_email(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        
        # Get the appointment object
        appointment = Appointment.objects.get(id=appointment_id)
        
        # Send acceptance email
        send_mail(
            'Appointment Accepted',
            'Dear {},\n\n' \
                      'We are pleased to inform you that your appointment has been accepted.\n\n' \
                      'Appointment Details:\n' \
                      '- Date: {}\n' \
                      '- Time: {}\n' \
                      '- Doctor: {}\n\n' \
                      'We look forward to seeing you.\n\n' \
                      'Best regards,\n' \
                      'HospitEase Team'.format(appointment.name, appointment.date, appointment.time, appointment.doctor),
            'from@example.com',
            [appointment.email],
            fail_silently=False,
        )
        
        # Redirect to a success page
        return HttpResponseRedirect('/success/')
    
