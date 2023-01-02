from django.db.models import Count
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import *
from .serializers import *
from .models import *

""" Api view for customizing token claims, this is useful when it comes to logging in user in the frontend """


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email,
        token["username"] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


"""Api View for listing all users and retrieving specific users using their id's"""


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        if self.request.method == 'GET':
            # Adds a new column that counts the number of accounts.
            return User.objects.annotate(number_of_accounts=Count('account'))
        return User.objects.all()


"""Api view to be used when a user first registers to the system"""


class RegisterAccountViewSet(CreateModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = UserAccountRegistrationSerializer


"""Api view for a user to add another new account"""


class AddUserAccountViewSet(ModelViewSet):
    serializer_class = AddAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}

    def get_queryset(self):
        return Account.objects.filter(user_id=self.kwargs['user_pk'])
