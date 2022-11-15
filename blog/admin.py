from django.contrib import admin

from blog.models import Profile, CustomUser

# Register your models here.
admin.site.register([Profile, CustomUser])
