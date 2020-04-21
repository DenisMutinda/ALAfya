from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

def profile(request):
    context = {
        "title": "home",
    }
    return render(request, 'profile.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def SignUp(request):
    form = UserCreationForm()
    context = {
        'title': 'Signup',
    }
    return render(request, 'signup.html', context)


def StudentBooking(request):
    context = {
        "title" : "Student Booking",
    }

    return render(request, "booking.html", context)

@login_required
def StaffBooking(request):
    pass

