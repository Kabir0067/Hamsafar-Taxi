from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

urlpatterns = [
    path('admin/', admin.site.urls),  # URL барои панели администратор

    # URL-ҳо барои кор бо JWT (Simple JWT) барои тасдиқи корбарон
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   

    # Ворид кардани URL-ҳои дохилӣ аз 'myapp'
    path('', include('myapp.urls')), 
]


