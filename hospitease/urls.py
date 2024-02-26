"""
URL configuration for Hospitease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import logintxt
from hospitease import views
from registration.views import signtxt
from login.views import logintxt
from login.views import loginst
from feedback.views import feedtxt
from appointment.views import book_appointment
from hospitease.views import dash

# from appointment.views import bkapt

urlpatterns = [
    # Home Page
    path('admin/', admin.site.urls),
    path('', views.home),
    path('templates/home.html', views.home),
    path('templates/facility.html',views.facility),
    path('templates/about.html/', views.about),
    path('templates/Login.html', views.login),
    path('templates/registration.html', views.registration),
    path('login/',logintxt),
    path('templates/registration.html',signtxt),
    path('templates/feed.html',views.feed),
    path('register/', signtxt, name='register'),
    path('login/', logintxt, name='login'),
    path('loginint/', loginst, name='loginst'),
    path("templates/Loginint.html",views.log),
    path('templates/Login_inst.html',views.logg),
   path('templates/appointment.html', views.appoint),
   path('appointment/',book_appointment,name='bookappointment'),
   

   
    # Facility
    path('templates/vac.html',views.vac),
    path('templates/xray.html',views.xray),
    path('templates/physio.html',views.physio),
    path('sono.html',views.sono),
    path('templates/patho.html',views.vac),
    path('templates/xray.html',views.vac),
    path('templates/mri.html',views.vac),
    path('templates/Ct.html',views.vac),

    path('templates/admindash.html',views.dash),
    ]