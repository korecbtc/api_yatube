from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = 'У Вас нет прав для изменения этой записи'

    def has_object_permission(self, request, view, obj):
        return (request.method == 'GET'
                or obj.author == request.user)
