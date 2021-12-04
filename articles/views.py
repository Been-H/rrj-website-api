from copy import Error
from django.db.utils import InternalError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from django.core import serializers
from django.db import IntegrityError

from .models import Article
from threads.models import Thread
from category.models import Category
from author_auth.models import AuthorUser
from author_auth.serializers import AuthorUserCreationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import ArticleSerializer, CreateArticleSerializer, ArticleUpdateSerializer

@api_view(['GET', 'POST'])
def articles(request):
    if request.method == 'GET':
        category_name = request.query_params['category']
        dash = request.query_params['dash']
        #this part is very similiar and works for some reason
        if dash == "True":
            if request.user.is_authenticated:
                articles = Article.objects.filter(author=request.user)
            else:
                return HttpResponse(status=401)
        # *end part*
        elif category_name:
            try:
                category = Category.objects.get(name__icontains=category_name)
            except:
                return HttpResponse(status=400, content="Category not found")
            articles = Article.objects.filter(category=category)
        else:
            articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        
        return Response(serializer.data)
    if request.method == 'POST':
        thread_not_found = "The thread you are posting to does not exist"
        thread_id = request.query_params['thread_id']

        if request.user.is_authenticated:
            author = request.user
            if thread_id:
                try:
                    thread = Thread.objects.get(id=thread_id)
                except:
                    return HttpResponse(status=400, content=thread_not_found)
            
            article = Article(author=request.user)
            category_object = Category.objects.get(name__icontains = request.data['category'])
            del request.data['category']
            serializer = CreateArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                # if len(Article.objects.get(title=request.data['title'])) != 0:
                #     return HttpResponse(status=400, content=title_not_unique) 
                article = serializer.save()
                article.category = category_object
                article.save()
                if thread_id:
                    thread.articles.add(Article.objects.get(id=article.id))
                    thread.authors.add(author) 
            else: 
                return HttpResponse(status=400)   

            return Response(serializer.data)
        else:
            return HttpResponse(status=401)
    

@api_view(['GET', 'PUT', 'DELETE'])
def article_access(request, id):
    if request.method == "GET":
        try:
            article = Article.objects.get(id=id)
        except:
            return HttpResponse(status=400)
        if not article:
            return HttpResponse(status=400)
        serializer = ArticleSerializer(article, many=False)
        return Response(serializer.data)
    if request.method == "PUT":
        error_message = "Make sure the title has text"
        article = Article.objects.get(id=id)

        if request.user == article.author:
            serializer = ArticleUpdateSerializer(instance=article, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        else:
            return HttpResponse(status=403)
    if request.method == 'DELETE':
        article = Article.objects.get(id=id)
        if request.user == article.author:
            article.delete()
        else:
            return HttpResponse(status=403)
        return Response('article deleted')




