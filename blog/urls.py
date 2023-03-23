from django.urls import include, path
from blog import views


urlpatterns = [
    path('',views.StoriList.as_view()),
    path('stori/<int:pk>/',views.StoriDetail.as_view()),
    path('stori/<int:pk>/publish/', views.StoriPublish.as_view()),
    path('category/',views.CategoryCreate.as_view(),name="create-category"),
    path('category/<int:pk>/',views.CategoryDetail.as_view(),name="category-detail"), #update, delete
    # path('<int:pk>/comments/', views.StoriCommentsList.as_view(),name="comment-details"),
    path('comment/<int:pk>/',views.StoriCommentsDetail.as_view(),name="comment-detail")
]