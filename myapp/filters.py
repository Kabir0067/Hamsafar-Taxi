import django_filters
from .models import User, Ride, Booking

class UserFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['email']

class RideFilter(django_filters.FilterSet):
    departure_city = django_filters.CharFilter(lookup_expr='icontains')
    destination_city = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ride
        fields = ['departure_city', 'destination_city']

class BookingFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Booking
        fields = ['status']
