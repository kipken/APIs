from flightApp.models import Flight, Passenger, Reservation
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed


# from rest_framework


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,write_only=True)
    password2 = serializers.CharField(required=True,write_only=True)

    # password2 = serializers.CharField(max_length=20)

    class Meta:
        model = Passenger
        fields = '__all__'
        extra_kwargs = {"password": {"write_only": True},
                        "password2": {"write_only": True},"last_login":{"write_only":True}}

    def create(self, validated_data):
        validated_data.pop("password2", None)
        instance = self.Meta.model(**validated_data)
        # validated_data['password'] = validated_data.get('password1')
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

    def validate(self, attrs):
        first_name = attrs.get("first_name")
        last_name = attrs.get("last_name")
        pass1 = attrs.get("password")
        pass2 = attrs.get("password2")
        print(pass1,pass2)
        if not first_name and last_name:
            raise serializers.ValidationError("Supply both first and last names!")
        if pass1 != pass2:
            raise serializers.ValidationError("Password missmatch!")
        attrs['password'] = pass1

        return attrs


class ReservationSerializer(serializers.ModelSerializer):
    flight_detail = FlightSerializer(source="flight", read_only=True)
    passenger_detail = PassengerSerializer(source="passenger", read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'
        # read_only_fields = []
        extra_kwargs = {"flight": {"write_only": True}, "passenger": {"write_only": True}}
