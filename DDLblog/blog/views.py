from django.shortcuts import get_object_or_404, render, redirect

from .models import Post
from .forms import CommentForm

# Create your views here.

def detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_detail', slug=post.slug)
    
    else:
        form = CommentForm()
        
    return render(request, 'blog/detail.html', {'post': post, 'form': form})
