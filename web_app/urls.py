from re import template
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.login, name="Login"),
    path('home/', views.landing, name="landing"),
    path("user_login/", views.user_login, name="user_login"),
    path("logout/", views.logout, name="logout"),
    path("reg/", views.reg, name="reg"),
    path("train_img/", views.train_img, name="train_img"),
    path("takeattendance/", views.takeattendance, name="takeattendance"),
    path("reg_student/", views.reg_student, name="regstudent")
]