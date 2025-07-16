from rest_framework.permissions import BasePermission, IsAuthenticated


class CustomIsAuthenticated(IsAuthenticated):
    message = "Login qilib keling brodar."


class IsAdmin(BasePermission):
    message = "Siz admin emassiz."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsManager(BasePermission):
    message = "Siz manager emassiz."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'


class IsSeller(BasePermission):
    message = "Siz seller emassiz."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'


class IsNormalUser(BasePermission):
    message = "Siz oddiy foydalanuvchi emassiz."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'
