#urls for inside app alafya

from django.contrib import admin
from django.urls import path, include
from alafya import views


urlpatterns = [
    path('', views.SignUp, name = "signup"),
    path('login', views.login, name = "login"),
    path('home/', views.profile, name = "home"),
    path('booking/', views.StudentBooking, name = 'StjdentBooking'),
]