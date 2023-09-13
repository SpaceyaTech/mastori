from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

admin.site.site_header = "SpaceYaTech CMS Admin"
admin.site.site_title = "SpaceYaTech Admin Portal"
admin.site.index_title = "Welcome to SpaceYaTech CMS"

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/", include('djoser.urls')),
    path("api/", include('djoser.urls.jwt')),

    path('',include('blog.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

     # Add the Spectacular views for Swagger documentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)

admin.site.site_header = "SpaceYaTech CMS Admin"
admin.site.site_title = "SpaceYaTech Admin Portal"
admin.site.index_title = "Welcome to SpaceYaTech CMS"
