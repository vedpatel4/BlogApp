from rest_framework.permissions import BasePermission
from rest_framework.pagination import PageNumberPagination

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100