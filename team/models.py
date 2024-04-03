from django.db import models

# Create your models here.
class Member(models.Model):

    name = models.CharField(max_length=24, verbose_name='Name')
    position = models.CharField(max_length=30, verbose_name='Position')
    search_field = models.CharField(max_length=30, verbose_name='Search Field')
    intro = models.TextField(max_length=200, verbose_name='Introduction')
    
    
    interests = models.TextField(max_length=80, verbose_name='Interests')

    
    user_photo = models.ImageField(upload_to='uploads/', null=True, verbose_name='User Photo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')  # Add the missing field
    email = models.EmailField(max_length=254, verbose_name='Email')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
