
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView  
from rest_framework.response import Response
from .models import Account 
from .serializers import UserSerializer
from rest_framework import status, permissions
from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import AllowAny

class GetUsers(ListAPIView):                                        
    queryset = Account.objects.all()                                                                                                   
    serializer_class = UserSerializer
    permission_classes=[]  

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class UpdateUser(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes=[permissions.AllowAny]   

    def get_queryset(self, *args, **Kwargs):
        user_id = self.kwargs.get('id')                                 
        return Account.objects.get(id = user_id)                           
  
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
