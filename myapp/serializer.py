from rest_framework import serializers
from .models import User, Ride, Booking, Payment, RatingReview, Notification



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 
                  'password', 'user_type', 'profile_picture', 'preferred_routes', 
                  'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

# Ride Serializer
class RideSerializer(serializers.ModelSerializer):
    driver = UserSerializer(read_only=True)  
    class Meta:
        model = Ride
        fields = ['ride_id', 'driver', 'departure_city', 'destination_city', 
                  'departure_time', 'available_seats', 'ride_status', 
                  'created_at', 'updated_at']

# Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    ride = RideSerializer(read_only=True)   
    passenger = UserSerializer(read_only=True) 

    class Meta:
        model = Booking
        fields = ['booking_id', 'ride', 'passenger', 'seats_booked', 
                  'booking_status', 'created_at', 'updated_at']

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)   

    class Meta:
        model = Payment
        fields = ['payment_id', 'booking', 'amount', 'payment_method', 
                  'payment_status', 'created_at', 'updated_at']

# RatingReview Serializer
class RatingReviewSerializer(serializers.ModelSerializer):
    ride = RideSerializer(read_only=True)   
    reviewer = UserSerializer(read_only=True)   
    reviewee = UserSerializer(read_only=True)   

    class Meta:
        model = RatingReview
        fields = ['rating_id', 'ride', 'reviewer', 'reviewee', 
                  'rating', 'review_text', 'created_at', 'updated_at']


# Notification Serializer
class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)   

    class Meta:
        model = Notification
        fields = ['notification_id', 'user', 'message', 
                  'notification_type', 'read_status', 'created_at', 'updated_at']




class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8)
    user_id = serializers.IntegerField(write_only=True)
