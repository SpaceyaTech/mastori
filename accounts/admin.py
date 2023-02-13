from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

"""
Registering user model to the admin and extending the UserAdmin so that the user admin page looks like the default user admin panel
List_display specifies the attributes that will appear on the admin page.
add_fieldsets specifies the attributes to be using when creating a user on the admin panel.
fieldsets specifies the additional user fields
"""
#@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
class AccountInline(admin.StackedInline):
    model= Account
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    inlines = [AccountInline]
        
    def has_add_permission (self, request):
        if self.model.objects.count() >= 2 :
            return False
        return super().has_add_permission(request)

admin.site.register(User, AccountsAdmin)
#admin.site.register(User, CustomUserAdmin)
admin.site.register(Account, )