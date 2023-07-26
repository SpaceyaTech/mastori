from rest_framework_nested import routers

from blog import views

from .views import (CategoryViewset, CommentViewset, StoriViewset,DraftStoriViewset)


router = routers.DefaultRouter()
router.register('mastori/drafts', DraftStoriViewset, basename="mastori_draft")
router.register('mastori', StoriViewset, basename="mastori")
router.register("categories", CategoryViewset, basename="categories")


comment_router = routers.NestedDefaultRouter(router, 'mastori', lookup='mastori')
comment_router.register('comment', CommentViewset,basename="comments")


urlpatterns = router.urls + comment_router.urls
