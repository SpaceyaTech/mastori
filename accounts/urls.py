from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('register', views.RegisterAccountViewSet, basename='register')

"""Nesting to enable an account to be created under an existing user"""
users_router = routers.NestedDefaultRouter(router, 'users', lookup='user')
users_router.register('add_account', views.AddUserAccountViewSet, basename='add_account')


urlpatterns = router.urls + users_router.urls