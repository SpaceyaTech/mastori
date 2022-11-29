
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

