from re import template
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', views.login, name="Login"),
    path('landing/', views.landing, name="landing"),
    path("welcome/", views.user_login, name="user_login")

]