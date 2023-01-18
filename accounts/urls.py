
from django.urls import path  
from accounts import views as api_views
from rest_framework.authtoken import views  
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('register', views.RegisterAccountViewSet, basename='register')

"""Nesting to enable an account to be created under an existing user"""
users_router = routers.NestedDefaultRouter(router, 'users', lookup='user')
users_router.register('add_account', views.AddUserAccountViewSet, basename='add_account')


urlpatterns = router.urls + users_router.urls
"""urlpatterns = [
        path('accounts/', api_views.AccountAllView.as_view(), name="account"),
        path('accounts/create', api_views.AccountCreate.as_view(),  name="create-account"),                                             
        path('account/<int:id>/', api_views.AccountDetailView.as_view(), name="account-detail"),

        path('users/', api_views.UserAllView.as_view(), name="user"),
        path('user/create', api_views.UserCreate.as_view(),  name="create-user"),                                             
        path('user/<int:id>/', api_views.UserDetailView.as_view(), name="user-detail"),

        path('api-token-auth/', views.obtain_auth_token),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        
  
]"""
