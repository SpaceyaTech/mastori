from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from blog.serializers import BlogSerializer
from blog.filters import StoriFilter
from blog.models import Stori
from .throttles import BlogRateThrottle
from accounts.permissions import IsOwner
# Create your views here.


class StoriViewSet(viewsets.ModelViewSet):
    queryset = Stori.objects.all()
    serializer_class = BlogSerializer
    throttle_classes = [UserRateThrottle, BlogRateThrottle]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StoriFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]

    # Associate user with the post

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
