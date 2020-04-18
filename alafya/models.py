from django.db import models
from django.contrib.auth import User 
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

#extend the user model

class User(AbstractUser):

    HALL_CHOICES = (
        ('Olympus','Olympus'),
        ('Valkyrie', 'Valkyrie'),
        ('Keza', 'Keza'),
        ('Kushinga', 'Kushinga'),
        ('Office', 'Office'),
        ('Athena', 'Athena'),
        ('Titans', 'Titans'),
        ('Gaga', 'Gaga'),
        ('Malaika', 'Malaika'),
        ('Jeshi', 'Jeshi'),
        ('Twawana', 'Twawana'),
        ('Classified', 'Classified'),
    )

    YEAR_GROUP = (
        ('Year 1', 'Year 1'),
        ('Year 2', 'Year 2'),
    )
    hall = models.CharField(max_length = 50, choices = HALL_CHOICES)
    year_group = models.CharField(max_length = 50, choices= YEAR_GROUP)

class StudentBooking(models.Model):
    #STATUS = (
     #  ('Pending', 'Pending'),
      #  ('Approved', 'Approved'),
      # ('Rejected', 'Rejected'),
    #)

    #customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    counsellor = models.ForeignKey(settings.AUTH_USER_MODEL.objects.filter(is_staff = True), null = True, on_delete = models.SET_NULL)
    reason = models.CharField(null=True, max_length=255)
    date = models.DateField(null = True)
    timeToBeUsedFrom = models.TimeField(null=True)
    #status = models.CharField(max_length = 200, null = True, choices = STATUS)
    date_created = models.DateTimeField(auto_now_add = True, null=True)
