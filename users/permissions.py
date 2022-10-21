from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_admin


class IsTeacher(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_teacher


class IsAccountant(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_accountant
