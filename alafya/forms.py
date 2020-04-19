from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from alafya.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2']


class StudentBookingForm(ModelForm):
    class Meta:
        model = StudentBooking
        fields = '__all__'


class StaffBookingForm(ModelForm):
    class Meta:
        model = StaffBooking
        fields = '__all__'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

