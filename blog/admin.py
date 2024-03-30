from django.contrib import admin
from .models import Post

from .models import Post, Category, Comment

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']
    

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    

class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user.username
            
            obj.author = obj.author.replace(' ', '-')
            
        super().save_model(request, obj, form, change)
    
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']   
    
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentItemInline]

    def get_inline_instances(self, request, obj=None):
        if obj and obj.comments.exists():
            return super().get_inline_instances(request, obj)
        return []

    

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)