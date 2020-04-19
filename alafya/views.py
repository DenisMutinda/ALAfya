from django.shortcuts import render, redirect
from django.conf import settings
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
    context = {}
    return render(request, 'home.html', context)


def login(request):
    pass


def SignUp(request):
    pass

def StudentBooking(request):
    pass

def StaffBooking(request):
    pass

