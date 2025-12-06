from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Tag(models.Model):
    """
    Tag model:
    - Allows labeling/categorizing posts.
    - Tags have unique names.
    - Posts can have multiple tags (ManyToMany).
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager() # for tagging functionality

    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
     # used by CreateView / UpdateView (or you can set success_url directly)  
        return reverse('post_detail', kwargs= {'pk': self.str})
class Comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.pk})