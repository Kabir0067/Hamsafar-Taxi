from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'email', 'phone_number', 'user_type', 'created_at', 'updated_at')
    list_filter = ('user_type', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('-created_at',)

class RideAdmin(admin.ModelAdmin):
    list_display = ('ride_id', 'driver', 'departure_city', 'destination_city', 'departure_time', 'available_seats', 'ride_status', 'created_at')
    list_filter = ('ride_status', 'driver', 'departure_city', 'destination_city')
    search_fields = ('departure_city', 'destination_city')
    ordering = ('-departure_time',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'ride', 'passenger', 'seats_booked', 'booking_status', 'created_at')
    list_filter = ('booking_status', 'ride', 'passenger')
    search_fields = ('ride__ride_id', 'passenger__first_name', 'passenger__last_name')
    ordering = ('-created_at',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'booking', 'amount', 'payment_method', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'booking')
    search_fields = ('booking__booking_id', 'amount')
    ordering = ('-created_at',)

class RatingReviewAdmin(admin.ModelAdmin):
    list_display = ('rating_id', 'ride', 'reviewer', 'reviewee', 'rating', 'created_at')
    list_filter = ('ride', 'rating', 'reviewer', 'reviewee')
    search_fields = ('ride__ride_id', 'reviewer__first_name', 'reviewee__first_name')
    ordering = ('-created_at',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'user', 'message', 'notification_type', 'read_status', 'created_at')
    list_filter = ('user', 'notification_type', 'read_status')
    search_fields = ('message',)
    ordering = ('-created_at',)


admin.site.register(User, UserAdmin)
admin.site.register(Ride, RideAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(RatingReview, RatingReviewAdmin)
admin.site.register(Notification, NotificationAdmin)
