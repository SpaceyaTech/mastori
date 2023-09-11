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

from drf_spectacular.utils import extend_schema,OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from accounts.models import Account
from blog.filters import StoriFilter
from blog.models import Category, Comment, Stori
from blog.serializers import (BlogSerializer, CategorySerializers,
                              CommentSerializer)

from .throttles import BlogRateThrottle
from .permissions import IsBlogOwnerOrReadOnly, IsCommentOwnerOrReadOnly

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
    
@extend_schema(responses=BlogSerializer)
class StoriViewset(viewsets.ModelViewSet):
    """"blog/stori viewset"""
    serializer_class = BlogSerializer
    queryset = Stori.objects.filter(status="Published")
    permission_classes = [IsAuthenticatedOrReadOnly, IsBlogOwnerOrReadOnly]

    def perform_create(self, serializer):
        # set account of logged in user to blog created before saving
        #account = Account.objects.get(user=self.request.user)
        serializer.save(created_by__user=self.request.user)

@extend_schema(responses=BlogSerializer, parameters=[OpenApiParameter(name="id", type=OpenApiTypes.INT)])
class DraftStoriViewset(viewsets.ModelViewSet):
    """"draft Stori viewset"""
    serializer_class = BlogSerializer
    http_method_names = ["get","put","delete","patch"]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Stori.objects.filter(status="Draft", created_by__user=self.request.user)
        return queryset

@extend_schema(responses=CommentSerializer, parameters=[ OpenApiParameter(name="mastori_pk", type=OpenApiTypes.INT)])
class CommentViewset(viewsets.ModelViewSet):
    """comment viewset"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsCommentOwnerOrReadOnly]

    def get_serializer_context(self):
        return {"blog_id":self.kwargs["mastori_pk"]}
    
    def get_queryset(self):
        return Comment.objects.filter(stori=self.kwargs["mastori_pk"])

    # set post and account in comment created before saving
    def perform_create(self, serializer):
        stori = Stori.objects.get(id=self.kwargs["mastori_pk"])
        account = Account.objects.get(user=self.request.user)
        serializer.save(stori=stori, account=account)

