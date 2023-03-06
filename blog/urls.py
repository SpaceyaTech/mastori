from django.urls import include, path
from blog import views


urlpatterns = [
    path('',views.StoriList.as_view()),
    path('stori/<int:pk>/',views.StoriDetail.as_view()),
    path('stori/<int:pk>/publish/', views.StoriPublish.as_view()),

    path('stori/<slug:slug>/viewers/', views.StoriViewersCountView.as_view(), name='stori-count'),
]