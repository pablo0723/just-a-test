from rest_framework.permissions import BasePermission, SAFE_METHODS

from component.personal.models import Profile


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return self.has_object_permission(request, view, None)

    def has_object_permission(self, request, view, obj):
        if obj is None:
            if view.kwargs.get('username') == request.user.username:
                return True

        if isinstance(obj, Profile):
            return request.user == obj
        return False
