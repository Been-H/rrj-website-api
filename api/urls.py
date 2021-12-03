import author_auth
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('articles/', include('articles.urls')),
    path('authors/', include('authors.urls')),
    path('author-auth/', include('author_auth.urls')),
    path('threads/', include('threads.urls')),
    path('categories/', include('category.urls')),
]