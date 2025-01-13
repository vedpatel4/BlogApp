from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from blogs.models import Blog
from rest_framework.exceptions import PermissionDenied

class CommentListView(ListAPIView):
    queryset = Blog.objects.filter(status='published')
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog_id=blog_id)

class CommentCreateView(CreateAPIView):
    queryset = Blog.objects.filter(status='published')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        blog_id = self.kwargs['blog_id']
        blog = Blog.objects.get(pk=blog_id)
        serializer.save(writer=self.request.user, blog=blog)

class CommentDeleteView(DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog_id=blog_id)

    def perform_destroy(self, instance):
        if instance.blog.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this comment.")
        instance.delete()