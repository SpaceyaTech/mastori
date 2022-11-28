
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView  
from rest_framework.response import Response
from .models import Account 
from .serializers import UserSerializer
from rest_framework import status, permissions



class GetUsers(ListAPIView):                                        
    queryset = Account.objects.all()                                                                                                   
    serializer_class = UserSerializer


class UpdateUser(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer


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
