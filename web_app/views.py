from django.contrib import messages
from turtle import home
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls.static import static
from django.contrib.auth import login,authenticate,logout
from web_app.models import StudentData
from web_app import take_attendance

# Create your views here.

def takeattendance(request):
    return render(request ,"cam_attendance.html")

def response(request):
    return HttpResponse("Working Fine!!!")

def login(request):
    return render(request, "login.html")


def landing(request):
    #created just for checking
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          print(username)
          print(password)
          user = authenticate(username=username, password=password)
          if user is not None:
                    #login(request, user)
            #if request.user.is_authenticated :
                    return redirect('/home')

          else:
                    messages.info(request, "Problem Logging in")
                    return redirect('/')
     

def logout(request):
    messages.info(request, "Logged out sucessfully")
    return redirect('Login')

def reg(request):
    return render(request, "register.html")


def train_img(request):
    return render(request, "camera.html")


def reg_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll = request.POST.get('roll')
        course = request.POST.get('course')
        stream = request.POST.get('strm')
        gender = request.POST.get('gender')
        year = request.POST.get('year')


        new_student = StudentData(name=name, email=email, roll=roll, course=course,  stream=stream, gender=gender, year=year)
        new_student.save()
        #take_attendance.create_dataset()


        return redirect('train_img')