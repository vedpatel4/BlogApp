from rest_framework import serializers
from .models import Blog, Category, Tag
from comments.serializers import CommentSerializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    comments = CommentSerializer(many = True, read_only=True)
    num_comments = serializers.IntegerField(source = 'comment_count', read_only=True)
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'tags', 'status', 'author', 'created_at','comments','num_comments']
        read_only_fields = ['author', 'created_at', 'comments', 'num_comments']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        category_data = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(**category_data)
        blog = Blog.objects.create(category=category,**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            blog.tags.add(tag)
        blog.save()
        return blog

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        category_data = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(**category_data)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.tags.clear()
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        instance.category = category
        instance.save()
        return instance

class BlogListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    num_comments = serializers.IntegerField(source='comment_count', read_only=True)
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'tags', 'status', 'author', 'created_at', 'num_comments']
        read_only_fields = ['title', 'content', 'tags', 'category', 'status', 'author', 'created_at', 'num_comments']
