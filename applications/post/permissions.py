from rest_framework.permissions import BasePermission, SAFE_METHODS

"""
user1, user2
post1, post2
"""
class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        # print(request.method)
        # print(request.user.is_authenticated)
        # print(SAFE_METHODS)
        return request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user == obj.owner
        