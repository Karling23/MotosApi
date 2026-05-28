from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow administrators to edit it.
    Read permissions are allowed to any request.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view/edit it.
    Admins have full access.
    """
    def has_object_permission(self, request, view, obj):
        # Admins have full access
        if request.user and request.user.is_staff:
            return True
        # For User model itself
        if hasattr(obj, 'username'):
            return obj == request.user
        # For models having a foreign key 'usuario'
        return hasattr(obj, 'usuario') and obj.usuario == request.user
