from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from accounts.models import Account
from accounts.serializers import AccountDetailSerializer, UserSerializer
from blog.filters import StoriFilter
from blog.models import Category, Comment, Stori
from blog.serializers import (BlogSerializer, CategorySerializers,
                              CommentSerializer)

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


class StoriPublish(generics.UpdateAPIView):
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




# class CategoryCreate(generics.ListCreateAPIView):

#     """ create a category """

#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     """ list all categories """

#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    
    def get_permissions(self):
        # admin is allowed to destroy and update a category
        if self.action == 'destroy' or self.action == "update":
            self.permission_classes = [IsAdminUser]
        # anyone can create, retrieve and list all categories
        elif self.action == 'retrieve' or self.action == "create" or self.action == "list":
            self.permission_classes = [AllowAny]
        return super().get_permissions()
    

class StoriViewset(viewsets.ModelViewSet):
    """"blog/stori viewset"""
    serializer_class = BlogSerializer
    queryset = Stori.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # set account of logged in user to blog created before saving
        account = Account.objects.get(user=self.request.user)
        serializer.save(created_by=account)


class CommentViewset(viewsets.ModelViewSet):
    """comment viewset"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {"blog_id":self.kwargs["mastori_pk"]}
    
    def get_queryset(self):
        return Comment.objects.filter(stori=self.kwargs["mastori_pk"])

    # set post and account in comment created before saving
    def perform_create(self, serializer):
        post = Stori.objects.get(id=self.kwargs["mastori_pk"])
        account = Account.objects.get(user=self.request.user)
        serializer.save(post=post, account=account)

# account/id/blog/id/comment/id/
# class AccountViewSet(viewsets.ViewSet):
#     """Serialize account"""
#     serializer_class = UserSerializer
#     authentication_classes = [SessionAuthentication]

#     def list(self, request):
#         queryset = Account.objects.filter()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         queryset= Account.objects.filter()
#         account = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(account)
#         return Response(serializer.data)


class AccountViewset(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = AccountDetailSerializer
    permission_classes = [IsAdminUser] # to allow owner
    queryset = Account.objects.all()
    

class BlogViewset(viewsets.ViewSet):
    serializer_class = BlogSerializer
    

    def list(self, request, accounts_pk=None):
        queryset = Stori.objects.filter(created_by=accounts_pk)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None, accounts_pk=None):
        queryset = Stori.objects.filter(created_by=accounts_pk,pk=pk)
        blog = get_object_or_404(queryset,pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)


class BlogCommentViewset(viewsets.ViewSet):
    """Comment viewset"""
    serializer_class = CommentSerializer


    def list(self, request, mastori_pk=None, accounts_pk=None):
        queryset = Comment.objects.filter(stori=mastori_pk, account=accounts_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None, mastori_pk=None, accounts_pk=None):
        queryset = Comment.objects.filter(pk=pk, stori=mastori_pk, account=accounts_pk)
        comments = get_object_or_404(queryset,pk=pk)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
        