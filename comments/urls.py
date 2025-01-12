from django.urls import path
from .views import CommentListView, CommentCreateView, CommentDeleteView

urlpatterns = [
    path('<int:blog_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('<int:blog_id>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:blog_id>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]