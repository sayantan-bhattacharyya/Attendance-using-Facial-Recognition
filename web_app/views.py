from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls.static import static
from django.contrib.auth import login,authenticate,logout
from .models import LoginDetails

# Create your views here.
def response(request):
    return HttpResponse("Working Fine!!!")

def login(request):
    return render(request, "login.html")


def landing(request):
    return render(request, 'landing.html')

def user_login(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
             
            try:
                user = LoginDetails.empAuth_objects.get(username=username,password=password)
                if user is not None:
                    messages.success(request, "Successfully Loged in")               
                    landing(request)
                else:
                    messages.error(request, "Problem Logging in")
                    print("Someone tried to login and failed.")
                    return redirect('login.html')

            except Exception as identifier:
                
                return redirect('login.html')
     
        else:
            return render(request, 'login.html')


