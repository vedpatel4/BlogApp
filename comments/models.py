from django.db import models
from users.models import CustomUser as User
from blogs.models import Blog

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.writer} on {self.blog}'
    
