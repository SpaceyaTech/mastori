from django.shortcuts import render
from  rest_framework.generics import ListAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from blog.serializers import BlogSerializer
from blog.filters import StoriFilter
from blog.models import Stori
from rest_framework.throttling import UserRateThrottle
from .throttles import BlogRateThrottle
from rest_framework.response import Response


# Create your views here.
class StoriList(ListAPIView):
    queryset = Stori.objects.all()   
    serializer_class = BlogSerializer
    throttle_classes = [UserRateThrottle, BlogRateThrottle]
    filter_backends = (DjangoFilterBackend,)   
    filterset_class = StoriFilter

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