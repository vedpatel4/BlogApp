from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializers import BlogSerializer, BlogListSerializer, BlogPublishSerializer
from .utils import IsAuthor, BlogPagination

class BlogListView(ListAPIView):
    queryset = Blog.objects.filter(status='published')
    serializer_class = BlogListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author', 'category', 'tags__name']
    search_fields = ['title', 'content', 'category__name', 'tags__name', 'author__username']
    pagination_class = BlogPagination

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.filter(status='published')
    serializer_class = BlogSerializer

class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        if 'status' in validated_data:
            validated_data.pop('status')
        serializer.save(author=self.request.user)

class BlogDeleteView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_destroy(self, instance):
        instance.delete()

class BlogPublishView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogPublishSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_update(self, serializer):
        serializer.save(status='published')