""""
- Only admin users can get a list of all users
- Only admin can delete users
- Everyone can create a user (register)
- Logged in user can only retrieve/update his own profile.

"""

from rest_framework import permissions


class IsLoggedInUserOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff