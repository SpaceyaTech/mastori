from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render, get_object_or_404
from accounts.models import Account
from rest_framework import viewsets
from blog.serializers import BlogSerializer, CommentSerializer, CategorySerializers
from blog.filters import StoriFilter
from blog.models import Stori,Comment,Category
from rest_framework.throttling import UserRateThrottle
from .throttles import BlogRateThrottle
from accounts.serializers import UserSerializer



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




class CategoryCreate(generics.ListCreateAPIView):

    """ create a category """

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """ list all categories """

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class StoriViewset(viewsets.ModelViewSet):
    """"blog/stori viewset"""
    serializer_class = BlogSerializer
    queryset = Stori.objects.all()

class CommentViewset(viewsets.ModelViewSet):
    """comment viewset"""
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {"blog_id":self.kwargs["blog_pk"]}
    
    def get_queryset(self):
        return Comment.objects.filter(Post_id=self.kwargs["blog_pk"])

# account/id/blog/id/comment/id/
class AccountViewSet(viewsets.ViewSet):
    """Serialize account"""
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]

    def list(self,request):
        queryset = Account.objects.filter()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        queryset= Account.objects.filter()
        account = get_object_or_404(queryset,pk=pk)
        serializer = UserSerializer(account)
        return Response(serializer.data)

class Blogviewset(viewsets.ViewSet):
    serializer_class = BlogSerializer
    

    def list(self,request,account_pk=None):
        queryset = Stori.objects.filter(created_by=account_pk)
        blogs = get_object_or_404(queryset,pk=pk)
        serializer = BlogSerializer(blogs)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None,account_pk=None):
        queryset = Stori.objects.filter(created_by=account_pk,pk=pk)
        blogs = get_object_or_404(queryset,pk=pk)
        serializer = BlogSerializer(blogs,many=True)
        return Response(serializer.data)

class BlogCommentViewSet(viewsets.ViewSet):
    """Comment viewset"""
    serializer_class = CommentSerializer

    def list(self, request,pk=None,blog_pk=None,account_pk=None):
        queryset = Comment.objects.filter(Post_id=blog_pk,user=account_pk)
        comments = get_object_or_404(queryset,pk=pk)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None,blog_pk=None,account_pk=None):
        queryset = Comment.objects.filter(pk=pk,Post_id=blog_pk,user=account_pk)
        comments = get_object_or_404(queryset,pk=pk)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
        
        
