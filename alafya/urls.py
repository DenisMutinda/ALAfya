#urls for inside app alafya

from django.contrib import admin
from django.urls import path, include
from alafya import views


urlpatterns = [
    path('', views.login),
]