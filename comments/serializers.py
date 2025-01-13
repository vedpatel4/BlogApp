from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
    writer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['writer', 'content', 'post_date']

    
    