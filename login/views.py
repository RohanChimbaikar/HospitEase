from django.shortcuts import render
import mysql.connector as sql
from appointment.models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, User
un=''
pw=''
# Create your views here.
def logintxt(request):
    global un,pw
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="123456789",database='hospitease')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="un":
                un=value
            if key=="pw":
                pw=value
        
        c="select * from registration where email='{}' and password='{}'".format(un,pw)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            # Retrieve the group object with the name "Doctor"
            doctor_group = Group.objects.get(name='Doctors')
            # Filter users based on the retrieved group
            doctor_users = User.objects.filter(groups=doctor_group)
            print(doctor_users)
            
            return render(request,"appointment.html",{'doctor_users': doctor_users})

    return render(request,'/templates/Login.html')

def loginst(request):
    appointments = Appointment.objects.all()
    global un,pw
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="123456789",database='hospitease')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="un":
                un=value
            if key=="pw":
                pw=value
        
        c="select * from registration_registration where username='{}' and password='{}'".format(un,pw)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"templates/docdash.html",{'appointments': appointments})

    return render(request,'Loginint.html')