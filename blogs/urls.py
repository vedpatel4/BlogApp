from django.urls import path
from .views import (
    BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogPublishView,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('<int:pk>/publish/', BlogPublishView.as_view(), name='blog-publish'),
]