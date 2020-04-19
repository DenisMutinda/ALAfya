from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from alafya.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model  = settings.AUTH_USER_MODEL
        fields = ['first_name','last_name','hall', 'year_group', 'email', 'password1', 'password2']


class StudentBookingForm(ModelForm):
    class Meta:
        model = StudentBooking
        fields = '__all__'


class StaffBookingForm(ModelForm):
    class Meta:
        model = StaffBooking
        fields = '__all__'

