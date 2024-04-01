from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage


from blog.models import Post, Category
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/frontpage.html', {'posts': posts})

def news(request):
    news_category = Category.objects.get(slug='news')  # or title='news' if you prefer
    posts = Post.objects.filter(Q(category=news_category) | Q(category2=news_category) | Q(category3=news_category))
    return render(request, 'core/news.html', {'posts': posts})

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

def about_lab(request):
    item = Category.objects.get(slug='about-lab')
    posts = Post.objects.filter(Q(category=item) | Q(category2=item) | Q(category3=item))
    return render(request, 'core/about_lab.html', {'posts': posts})

def about_team(request):
    item = Category.objects.get(slug='about-team')
    posts = Post.objects.filter(Q(category=item) | Q(category2=item) | Q(category3=item))
    return render(request, 'core/about_team.html', {'posts': posts})

def contact(request):

    return render(request, 'core/contact.html')

@csrf_exempt
def upload(request):
    print(request.FILES)  # print the FILES attribute of the request
    if request.method == 'POST':
        upload = request.FILES.get('upload')
        if upload is not None:
            name = default_storage.save(upload.name, upload)
            url = default_storage.url(name)
            return JsonResponse({
                'uploaded': 1,
                'fileName': name,
                'url': url,
            })
        else:
            return JsonResponse({'error': 'No file was uploaded'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)