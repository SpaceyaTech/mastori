"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from accounts.views import MyTokenObtainPairView

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "SpaceYaTech CMS Admin"
admin.site.site_title = "SpaceYaTech Admin Portal"
admin.site.index_title = "Welcome to SpaceYaTech CMS"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('blog/',include('blog.urls')),


    path("", include("accounts.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)

admin.site.site_header = "SpaceYaTech CMS Admin"
admin.site.site_title = "SpaceYaTech Admin Portal"
admin.site.index_title = "Welcome to SpaceYaTech CMS"
