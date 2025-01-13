from django.db import models
from users.models import CustomUser as User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    # Status options for the blog post: 'draft' for unpublished, 'published' for public posts.
    STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ]

    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(null=True, blank=True, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def comment_count(self):
        # Returns the total number of comments related to this blog post.
        return self.comment_set.count()

