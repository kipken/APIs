from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, ReservationViewSet, PassengerViewSet,find_flights,save_reservation,find_passenger
from django.urls import path,include

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)
router.register('reservations', ReservationViewSet)

url_patterns = [
    path('',include(router.urls)),
    path('findFlight/',find_flights),
    path('retrieve_passenger/',find_passenger),
    path('reserve_flight/',save_reservation)
]
