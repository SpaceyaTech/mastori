
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
"""
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView  
from rest_framework.response import Response
from .models import Account, User
from .serializers import AccountSerializer, UserSerializer
from rest_framework import status, permissions



class AccountAllView(ListAPIView):                                        
    queryset = Account.objects.all()                                                                                                   
    serializer_class = AccountSerializer

class AccountCreate(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #permission_classes=[permissions.AllowAny]


class AccountDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer

 
    def get_queryset(self, *args, **Kwargs):
        account_id = self.kwargs.get('id')                                 
        return Account.objects.get(id = account_id )                           

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        account = self.get_queryset(id)
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    def put(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        account = self.get_queryset(id) 
        serializer = AccountSerializer(account, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        account = self.get_queryset(id) 
        account.delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)



class UserAllView(ListAPIView):                                        
    queryset = User.objects.all()                                                                                                   
    serializer_class = UserSerializer

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes=[permissions.AllowAny]


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

   
    def get_queryset(self, *args, **Kwargs):
        user_id = self.kwargs.get('id')                                 
        return User.objects.get(id=user_id)                           
  
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user = self.get_queryset(id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user = self.get_queryset(id) 
        serializer = UserSerializer(user, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user = self.get_queryset(id) 
        user.delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
"""
