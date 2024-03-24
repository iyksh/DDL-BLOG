from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title',]

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)