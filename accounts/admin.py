from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

"""
Registering user model to the admin and extending the UserAdmin so that the user admin page looks like the default user admin panel
List_display specifies the attributes that will appear on the admin page.
add_fieldsets specifies the attributes to be using when creating a user on the admin panel
"""
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Account)