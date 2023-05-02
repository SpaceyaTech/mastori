from django.urls import include, path
from rest_framework_nested import routers

from accounts.views import UserViewSet
from blog import views

from .views import (AccountViewset, BlogCommentViewset, BlogViewset,
                    CategoryViewset, CommentViewset, StoriViewset)

urlpatterns = [
    path('',views.StoriList.as_view()),
    # path('<int:pk>/comments/',views.StoriDetail.as_view(),name="blog-detail"),
    # path('stori/<int:pk>/publish/', views.StoriPublish.as_view()),
    # path('category/',views.CategoryCreate.as_view(),name="create-category"),
    # path('category/<int:pk>/',views.CategoryDetail.as_view(),name="category-detail"), #update, delete
    # path('comment/<int:pk>/',views.StoriCommentsDetail.as_view(),name="comment-detail"),#view a specific comment
    # path('<int:pk>/comment/',views.StoriCommentCreate.as_view(),name="create-comment"),#specific comment 
]
# blogs/id/comments/id
router = routers.DefaultRouter()
router.register('blogs', StoriViewset, basename="blogs")


stori_router = routers.NestedDefaultRouter(router, 'blogs', lookup='blogs')
stori_router.register('comments', CommentViewset,basename="comments")

# accounts/id/blogs/id/comments/id/
account_router = routers.DefaultRouter()
account_router.register("accounts", AccountViewset, basename="accounts")

blog_router = routers.NestedDefaultRouter(account_router, "accounts", lookup="accounts")
blog_router.register("blogs", BlogViewset, basename="blogs")

comment_router = routers.NestedDefaultRouter(blog_router, "blogs", lookup="blogs")
comment_router.register("comments", BlogCommentViewset, basename="comments")

# categories/id/
category_router = routers.DefaultRouter()
category_router.register("categories", CategoryViewset, basename="categories")

urlpatterns = router.urls + stori_router.urls \
    + account_router.urls + blog_router.urls \
        + comment_router.urls + category_router.urls
