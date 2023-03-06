from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.throttling import UserRateThrottle

from django_filters.rest_framework import DjangoFilterBackend

from blog.models import Stori
from blog.serializers import BlogSerializer, StoriViewersSerializer
from blog.filters import StoriFilter
from blog.throttles import BlogRateThrottle






# Create your views here.
# class StoriList(ListAPIView):
#     queryset = Stori.objects.all()   
#     serializer_class = BlogSerializer
#     throttle_classes = [UserRateThrottle, BlogRateThrottle]
#     filter_backends = (DjangoFilterBackend,)   
#     filterset_class = StoriFilter
    

"""List and create mastori using ListCreateAPIView"""
class StoriList(generics.ListCreateAPIView):
    queryset = Stori.objects.all()
    serializer_class = BlogSerializer
    throttle_classes = [UserRateThrottle, BlogRateThrottle]
    filter_backends = (DjangoFilterBackend,)   
    filterset_class = StoriFilter

"""Fetch, Update and Delete an individual stori"""
class StoriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stori.objects.all()
    serializer_class = BlogSerializer


class StoriPublish(UpdateAPIView):
    queryset = Stori.objects.all()
    serializer_class = BlogSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'published'
        instance.save()
        instance.publish()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StoriViewersCountView(APIView):
    """Count the numbers of account that views a stori"""
    def get(self, request, slug, format=None):
        try:
            stori = Stori.objects.get(slug=slug)
        except Stori.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StoriViewersSerializer(stori)
        return Response(serializer.data)
