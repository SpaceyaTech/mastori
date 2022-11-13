from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



from post.api.views import (
single_post_detail,
all_posts,
update_post,
delete_post,
create_post,
)
   


app_name = "post"

urlpatterns = [
    path("create", create_post, name="create_post"),
    path("<int:pk>/", single_post_detail, name="single_post"),
    path("all/", all_posts, name="all_posts"),
    path("<int:pk>/edit", update_post, name="update_post"),
    path("<int:pk>/delete", delete_post, name="delete_post"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)