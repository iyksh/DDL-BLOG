from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, verbose_name='Category 1')
    category2 = models.ForeignKey(Category, related_name='posts2', on_delete=models.CASCADE, verbose_name='Category 2')
    category3 = models.ForeignKey(Category, related_name='posts3', on_delete=models.CASCADE, verbose_name='Category 3')
    
    title = models.CharField(max_length=124, verbose_name='Title')
    slug = models.SlugField(verbose_name='Slug (e.g. hello-world)')
    intro = models.TextField(blank=True, verbose_name='Introduction')
    body = CKEditor5Field(blank=True, null=True, verbose_name='Content')    
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Banner Image')
    author = models.CharField(max_length=255, default='It will be automatically filled in.', editable=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name