from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only access to unauthenticated users
    and full access to authenticated users.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Require authentication for other request methods
        return request.user and request.user.is_authenticated
