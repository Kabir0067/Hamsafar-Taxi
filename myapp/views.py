from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    
    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()] 
        if self.action == 'list':  
            return [IsAdminUser()]
        if self.action == 'destroy':  
            return [IsAdminUser()]
        return super().get_permissions()



class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    filterset_class = RideFilter
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsDriver()]   
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedUser()]   
        return super().get_permissions()
   
   
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_class = BookingFilter
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsPassenger()]   
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedUser()]   
        if self.action == 'destroy':
            return [IsPassenger()]   
        return super().get_permissions()



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [IsAuthenticatedUser()]   
        return super().get_permissions()
   
    
class RatingReviewViewSet(viewsets.ModelViewSet):
    queryset = RatingReview.objects.all()
    serializer_class = RatingReviewSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [IsAuthenticatedUser()]   
        return super().get_permissions()
    

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_permissions(self):
        return [IsAuthenticatedUser()]  
    



class RequestPasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        
        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            
            reset_url = request.build_absolute_uri(reverse('password-reset-confirm', args=[token]))
            
            send_mail(
                'Барқарор кардани пароли шумо',
                f'Барои барқарор кардани пароли худ, лутфан ба пайванди зерин равед: {reset_url}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return Response({'success': 'Пайванд барои барқарор кардани парол ба почтаи шумо равон шуд.'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Корбар бо ин почта ёфт нашуд.'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request, token):
        password = request.data.get('password')
        user_id = request.data.get('user_id')
        
        user = User.objects.get(pk=user_id)
        token_generator = PasswordResetTokenGenerator()
        
        if token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            return Response({'success': 'Парол бомуваффақият навсозӣ шуд.'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Токен нодуруст ё мӯҳлати он гузаштааст.'}, status=status.HTTP_400_BAD_REQUEST)
