from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.categories, name="categories"),
    path('<str:name>', views.category, name="category"),
]
