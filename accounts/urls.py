from django.urls import path  
from . import views   



urlpatterns = [
        path('user/', views.GetUsers.as_view()),                                             
        path('user/<int:id>', views.UpdateUser.as_view()),  
]
