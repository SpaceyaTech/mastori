from django.urls import include, path
from blog import views


urlpatterns = [
    path('',views.StoriList.as_view()),
 
]