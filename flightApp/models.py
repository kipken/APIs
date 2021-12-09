from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# Create your models here.
# user model for authentication

# contains all the details of a flight
class Flight(models.Model):
    flight_no = models.CharField(max_length=25)
    operating_airlines = models.CharField(max_length=25)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    estimate_dep_time = models.TimeField()


# contains details of a passenger
class Passenger(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=200)
    email = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    # password1 = models.CharField(max_length=20,default="12345")
    # password2 = models.CharField(max_length=20,default="12345")
    groups = None
    user_permissions = None
    username = None


# when a reservation ought to be made
# uses the two models above to make a reservation
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
