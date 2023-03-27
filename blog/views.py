from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from accounts.models import Account
from blog.serializers import BlogSerializer, CommentSerializer, CategorySerializers
from blog.filters import StoriFilter
from blog.models import Stori,Comment,Category
from rest_framework.throttling import UserRateThrottle
from .throttles import BlogRateThrottle




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
    authentication_classes = [SessionAuthentication]
    throttle_classes = [UserRateThrottle, BlogRateThrottle]
    filter_backends = (DjangoFilterBackend,)   
    filterset_class = StoriFilter

    def perform_create(self, serializer):
        account_instance = Account.objects.get(user = self.request.user)
        return serializer.save(created_by=account_instance)


"""Fetch, Update and Delete an individual stori"""
class StoriDetail(generics.RetrieveAPIView):
    queryset = Stori.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication]

class StoriPublish(UpdateAPIView):
    queryset = Stori.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'published'
        instance.save()
        instance.publish()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StoriCommentCreate(generics.ListCreateAPIView):
    """Create, specific comment"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication]

    def perform_create(self, serializer):
        account_instance = Account.objects.get(user = self.request.user)
        return serializer.save(user=account_instance)


class StoriCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    """ get, update, destroy comment  """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication]
    


class CategoryCreate(generics.ListCreateAPIView):

    """ create a category """

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """ list all categories """

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

