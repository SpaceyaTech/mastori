from django.urls import path, re_path
from .views import LogoutAPIView, LoginAPIView
from rest_framework_simplejwt.views import (TokenRefreshView,TokenObtainPairView,)
from .views import *

urlpatterns = [
          
    path ('login/',LoginAPIView.as_view(), name = 'login'),
    path ('logout/',LogoutAPIView.as_view(), name = 'logout'),
    path ('token/refresh',TokenRefreshView.as_view(), name = 'token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    ]