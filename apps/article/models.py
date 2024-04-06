from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    like = models.ManyToManyField(User, related_name='like_posts', blank=True)
    dislike = models.ManyToManyField(User, related_name='dislike_posts', blank=True)
    
    class Meta:
        ordering = ['-created_at']
        

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    like = models.ManyToManyField(User, related_name='like_comments', blank=True)
    dislike = models.ManyToManyField(User, related_name='dislike_comments', blank=True)
    
    
    class Meta:
        ordering = ['-created_at']
        
    def  __str__(self):
        return self.content
