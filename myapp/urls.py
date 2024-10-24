from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequestPasswordResetView, PasswordResetConfirmView
from .views import *


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rides', RideViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'ratingreviews', RatingReviewViewSet)
router.register(r'notifications', NotificationViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('report/<int:pk>/', CustomReportView.as_view(), name='custom_report'),
    path('average-attendance/', CustomAverageAttendance.as_view(), name='custom_average_attendance'),


    path('request-password-reset/', RequestPasswordResetView.as_view(), name='request_password_reset'),
    path('password-reset-confirm/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]