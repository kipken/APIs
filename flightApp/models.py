from django.db import models


# Create your models here.
# contains all the details of a flight
class Flight(models.Model):
    flight_no = models.CharField(max_length=25)
    operating_airlines = models.CharField(max_length=25)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    estimate_dep_time = models.TimeField()


# contains details of a passenger
class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=200)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)


# when a reservation ought to be made
# uses the two models above to make a reservation
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
