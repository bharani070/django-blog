"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as BlogsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('posts/<slug:post_slug>/', BlogsViews.blogs, name='blogs'),
    
    # search path
    path('blogs/search/', BlogsViews.search, name='search'),

    # registration
    path('search/', views.registration, name='registration'),

    # signin
    path('signin/', views.signin, name='signin'),

    # signOut
    path('singout/', views.singout, name='signout'),

    # dashboard
    path('dashboard/', include('dashboards.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
