from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth import authenticate,login
# Create your views here.
def register(request):
    if request.method=='POST':
        your_name=request.POST.get('yrname')
        em=request.POST.get('email')
        pass1=request.POST.get('pass')
        pass2=request.POST.get('pass2')
        print(your_name,em,pass1,pass2)
        my_user=User.objects.create_user(your_name,em,pass1)
        my_user.save()
        return redirect('red')
    return render(request,'staffreg.html')


def logstaff(request):
    if request.method == "POST":
        uname = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(request, username=uname, password=pw)
        if user is not None:
            login(request, user)
            # Redirect to the dashboard upon successful login
            return redirect('templates/docdash.html')  # Assuming 'docdash' is the name of the URL pattern for the dashboard
        else:
            # Handle incorrect credentials
            return render(request, 'Loginint.html', {'error_message': 'Invalid username or password'})
    else:
        # Render the login page for GET requests
        return render(request, 'Loginint.html')





