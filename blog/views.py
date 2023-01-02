from django.shortcuts import render
from  rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from blog.serializers import BlogSerializer
from blog.filters import StoriFilter
from blog.models import Stori


# Create your views here.
class StoriList(ListAPIView):
    queryset = Stori.objects.all()   
    serializer_class = BlogSerializer  
    filter_backends = (DjangoFilterBackend,)   
    filterset_class = StoriFilter