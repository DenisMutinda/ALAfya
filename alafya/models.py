from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model as user_model
#from django.conf import settings


# Create your models here.

#extend the user model

class Profile(models.Model):

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hall = models.CharField(max_length = 50, choices = HALL_CHOICES)
    year_group = models.CharField(max_length = 50, choices= YEAR_GROUP)


#student booking
class StudentBooking(models.Model):
    #STATUS = (
     #  ('Pending', 'Pending'),
      #  ('Approved', 'Approved'),
      # ('Rejected', 'Rejected'),
    #)

    #customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    counsellor = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    reason = models.CharField(null=True, max_length=255)
    date = models.DateField(null = True)
    timeToBeUsedFrom = models.TimeField(null=True)
    #status = models.CharField(max_length = 200, null = True, choices = STATUS)
    date_created = models.DateTimeField(auto_now_add = True, null=True)


#staff booking
class StaffBooking(models.Model):
    STATUS = (
       ('Pending', 'Pending'),
       ('Approved', 'Approved'),
      ('Rejected', 'Rejected'),
     )

    student = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    reason = models.CharField(null=True, max_length=255)
    date = models.DateField(null = True)
    bookingTime = models.TimeField(null=True)
    bookingStatus = models.CharField(max_length = 200, null = True, choices = STATUS)
    date_created = models.DateTimeField(auto_now_add = True, null=True)