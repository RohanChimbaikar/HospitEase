from django.http import HttpResponse
from django.shortcuts import render 
from appointment.models import Appointment
from django.contrib.auth.decorators import login_required
from inventory.models import Product
from room_mgmt.models import Room
from django.shortcuts import render, redirect, get_object_or_404
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

def patho(request):
    return render(request,"templates/patho.html")

def mri(request):
    return render(request,"templates/mri.html")

def ct(request):
    return render(request,"templates/ct.html")

def log(request):
    
    return render(request,"templates/Loginint.html")

def logg(request):
    return render(request,"templates/Login_inst.html")

def appoint(request):
    return render(request,"appointment.html")

def dash(request):
    return render(request,"templates/admindash.html")


def invent(request):
    products = Product.objects.all()
    return render(request,"templates/docdash.html",{'products': products})


def doc(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.all()  # Query all appointments if it's not a POST request
        products = Product.objects.all()
        available_rooms = Room.objects.filter(available=True)
        unavailable_rooms = Room.objects.filter(available=False)
        return render(request, 'docdash.html', {
            "data": appointments,
            'products': products,
            'available_rooms': available_rooms,
            'unavailable_rooms': unavailable_rooms
        })
    else:
        return render(request, "templates/Loginint.html")

def book_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.available = False
    room.save()
    return redirect('doc')

def release_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.available = True
    room.save()
    return redirect('doc')

def occupy_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.available = False
    room.save()
    return redirect('doc')  # Redirect to the doc page after occupying the room

def unoccupy_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.available = True
    room.save()
    return redirect('doc')

    # def docdash(request):
    # Assuming there's a logged-in doctor
    # if request.user.is_authenticated:
    #     doctor = request.user  # Assuming the doctor is stored in the request.user object
    #     appointments = Appointment.objects.all()
    #     appointments = Appointment.objects.filter(doctor=doctor)
    #     return render(request, 'docdash.html', {'appointments': appointments})
    # else:
    #     # Handle case where there's no logged-in doctor or doctor doesn't exist
    #     return render(request, 'error.html', {'message': 'You are not logged in as a doctor or do not have any appointments.'})
    


def staffreg(request):
    return render(request,'templates/staffreg.html')

