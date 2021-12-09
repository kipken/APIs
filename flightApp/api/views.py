from django.shortcuts import render
from rest_framework.decorators import api_view

from flightApp.models import Passenger, Flight, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# create a function based view to handle find flights
# since this is a function based view, @api-view decorator ought to be imported and used
@api_view(["POST"])
def find_flights(request):
    flights = Flight.objects.filter(departure_city=request.data["departure_city"],
                                    arrival_city=request.data["arrival_city"])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def find_passenger(request):
    # returns the passenger based on the email and phone number supplied
    passengers = Passenger.objects.filter(email=request.data["email"], phone_number=request.data["phone_number"])
    serializer = PassengerSerializer(passengers, many=True)

    return Response(serializer.data)


# save a reservation, ensure the models have requisite relationships
# i.e for this instance, the flight model with reservation -- many_to_one relationship
#  many reservations could be made for a single flight
@api_view(["POST"])
def save_reservation(request):
    # retrieve flight details
    flight = Flight.objects.get(id=request.data['flightId'])
    # create a serializer for passenger to ensure that everything is validated before being saved

    # append passenger information here
    passenger = Passenger()
    passenger.first_name = request.data["first_name"]
    passenger.last_name = request.data["last_name"]
    passenger.middle_name = request.data["middle_name"]
    passenger.email = request.data["email"]
    passenger.phone_number = request.data["phone_number"]
    passenger.save()
    # instantiate Reservation model
    # assign it the required models for use
    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
