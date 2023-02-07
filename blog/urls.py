from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()
router.register("blog", views.StoriViewSet, basename="blog")

urlpatterns = [
    path('', include(router.urls)),

]
