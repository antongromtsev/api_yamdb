from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE':
            return request.user.role in ['admin', 'moderator']

        return obj.author == request.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_staff or request.user.role in ('admin')


class IsAuthenticatedOrAdmin(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return super(IsAuthenticated, self).has_permission(request, view)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_staff or request.user.role == 'admin'