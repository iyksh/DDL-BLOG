from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Category
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def news(request):
    news_category = Category.objects.get(slug='news')  # or title='news' if you prefer
    posts = Post.objects.filter(category=news_category)
    return render(request, 'core/news.html', {'posts': posts})

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

def about_lab(request):
    about_lab_category = Category.objects.get(slug='about-lab')  # or title='about-lab' if you prefer
    posts = Post.objects.filter(category=about_lab_category)
    return render(request, 'core/about_lab.html', {'posts': posts})
