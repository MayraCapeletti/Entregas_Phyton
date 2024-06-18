from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField # type: ignore

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300,  blank=True, null=True)
    body = RichTextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(upload_to='blog_images/',  blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=False)  
    def __str__(self):
        return f"comentario de {self.name} {self.content}"