from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    # The 'writer' field is read-only and will be automatically set to the requesting user during comment creation
    writer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['writer', 'content', 'post_date']

    
    