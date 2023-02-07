from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ 
    custom permission to only allow owners of object to edit, delete or update
    """

    def has_object_permission(self, request, view, obj):
        # allow GET methods
        if request.method in permissions.SAFE_METHODS:
            return True
        # PUT, DELETE only allowed to the owner
        return obj.owner == request.user
