from django.urls import include, path
from rest_framework_nested import routers
from blog import views
from .views import StoriViewset, CommentViewset

urlpatterns = [
    # path('',views.StoriList.as_view()),
    path('<int:pk>/comments/',views.StoriDetail.as_view(),name="blog-detail"),
    # path('stori/<int:pk>/publish/', views.StoriPublish.as_view()),
    # path('category/',views.CategoryCreate.as_view(),name="create-category"),
    # path('category/<int:pk>/',views.CategoryDetail.as_view(),name="category-detail"), #update, delete
    # path('comment/<int:pk>/',views.StoriCommentsDetail.as_view(),name="comment-detail"),#view a specific comment
    # path('<int:pk>/comment/',views.StoriCommentCreate.as_view(),name="create-comment"),#specific comment 
]
router = routers.DefaultRouter()
router.register('blog',StoriViewset,basename="blog" )

stori_router = routers.NestedDefaultRouter(router, 'blog',lookup='blog')
stori_router.register('comment', CommentViewset,basename="comment")


urlpatterns = router.urls + stori_router.urls
