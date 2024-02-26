from django.shortcuts import render
import mysql.connector as sql
from appointment.models import Appointment
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
            return render(request,"patientdash.html")

    return render(request,'Login.html')

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