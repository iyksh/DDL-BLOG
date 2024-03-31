"""crashblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include

from .sitemaps import CategorySitemap, PostSitemap


from core.views import robots_txt, upload
from core.views import frontpage, news
from core.views import about_lab, about_team

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    
    # DEFAULT #
    
    #===========================================================================
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('media/uploads/', upload, name='ck_editor_5_upload_file'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    #===========================================================================
    
    # HOME AND NEWS #
    
    #===========================================================================
    path('', frontpage, name='frontpage'),
    path('news/', news, name='news'),
    #===========================================================================
    
    # ABOUT #
    
    #===========================================================================
     path('about_lab', about_lab, name='about_lab'),
     path('about_team', about_team, name='about_team'),
     #path('contact/', about, name='contact'),
    #===========================================================================
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
