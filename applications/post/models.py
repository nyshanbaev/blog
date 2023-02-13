from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField('Название поста', max_length=50, null=True, blank=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images', null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.title}'  


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return f'{self.post.title}'
    

