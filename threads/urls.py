from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.threads, name='threads'),
    path('<int:id>', views.thread, name='thread'),
]
