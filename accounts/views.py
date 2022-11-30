from django.db.models import Count
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from accounts.models import *
from .serializers import *
from .models import *


"""Api View for listing all users and retrieving specific users using their id's"""
class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        if self.request.method == 'GET':
            return User.objects.annotate(number_of_accounts=Count('account'))#Adds a new column that counts the number of accounts.
        return User.objects.all()


"""Api view to be used when a user first registers to the system"""
class RegisterAccountViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = UserAccountRegistrationSerializer
    permission_classes = [IsAdminUser]


"""Api view for a user to add another new account"""
class AddUserAccountViewSet(ModelViewSet):
    serializer_class = AddAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}

    def get_queryset(self):
        return Account.objects.filter(user_id=self.kwargs['user_pk'])
