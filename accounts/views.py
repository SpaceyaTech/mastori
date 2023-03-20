from django.db.models import Count
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle 
from .throttles import AccountsRateThrottle
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import *
from .serializers import *
from .models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ 
    Api view for customizing token claims, this is useful when it comes to logging in user in the frontend
    """

    throttle_classes = [UserRateThrottle, AccountsRateThrottle]
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email,
        token["username"] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [UserRateThrottle, AccountsRateThrottle]
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """Api View for listing all users and retrieving specific users using their id's"""

    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle, AccountsRateThrottle]
    
    def get_queryset(self):
        if self.request.method == 'GET':
            # Adds a new column that counts the number of accounts.
            return User.objects.annotate(number_of_accounts=Count('account'))
        return User.objects.all()


class RegisterAccountViewSet(CreateModelMixin, GenericViewSet):
    """Api view to be used when a user first registers to the system"""

    queryset = Account.objects.all()
    serializer_class = UserAccountRegistrationSerializer
    throttle_classes = [UserRateThrottle, AccountsRateThrottle]


