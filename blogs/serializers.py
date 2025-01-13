from rest_framework import serializers
from .models import Blog, Category, Tag
from comments.serializers import CommentSerializer
class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    class Meta:
        model = Tag
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    class Meta:
        model = Category
        fields = ['name']

# Serializer for detailed Blog view, including tags, category, comments, and comment count
class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    comments = CommentSerializer(many=True, read_only=True)
    num_comments = serializers.IntegerField(source='comment_count', read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'tags', 'status', 'author', 'created_at', 'comments', 'num_comments']
        read_only_fields = ['author', 'created_at', 'comments', 'num_comments']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        category_data = validated_data.pop('category')

        # Get or create the category
        category, created = Category.objects.get_or_create(name = category_data["name"])

        blog = Blog.objects.create(category=category, **validated_data)

        # Link existing or new tags to the blog
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name = tag_data["name"])
            blog.tags.add(tag)
        
        blog.save()
        return blog

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        category_data = validated_data.pop('category')
        
        # Get or create the updated category
        category, created = Category.objects.get_or_create(name=category_data["name"])
        instance.category = category
        
        # Clear and update tags
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data["name"])
            instance.tags.add(tag)
        
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


# Serializer for listing blogs with minimal details
class BlogListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    num_comments = serializers.IntegerField(source='comment_count', read_only=True)
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'tags', 'status', 'author', 'created_at', 'num_comments']
        read_only_fields = ['title', 'content', 'tags', 'category', 'status', 'author', 'created_at', 'num_comments']


# Serializer to handle blog publishing (status change)
class BlogPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['status']