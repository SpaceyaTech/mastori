from rest_framework import viewsets
from rest_framework import permissions
from .models import User
from .serializer import UserSerializer,LoginSerializer,LogoutSerializer
from rest_framework import viewsets, generics,status,views
from rest_framework.response import Response
from .permission import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

        # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class LoginAPIView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes=[permissions.AllowAny]
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception= True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class=LogoutSerializer
    permission_classes=(permissions.IsAuthenticated,)

    def post(self, request):
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
