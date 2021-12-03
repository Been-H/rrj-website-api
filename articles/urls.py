from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:id>', views.article_access, name='article'),
]
