from copy import Error
from django.db.utils import InternalError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from django.core import serializers
from django.db import IntegrityError

from .models import Thread
from author_auth.models import AuthorUser
from category.models import Category
from author_auth.serializers import AuthorUserCreationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import CreateThreadSerializer, ThreadSerializer

@api_view(['GET', 'POST'])
def threads(request):
    if request.method == 'GET':
        dash = request.query_params['dash']
        category_name = request.query_params['category']
        if category_name:
            try:
                category = Category.objects.get(name__icontains=category_name)
            except:
                return HttpResponse(status=400, content="Category not found")
            threads = Thread.objects.filter(category=category)
        elif dash == "True":
            if request.user.is_authenticated:
                threads = Thread.objects.filter(authors=request.user)
            else:
                return HttpResponse(status=401)
        else:
            threads = Thread.objects.all()
        serializer = ThreadSerializer(threads, many=True)
        
        return Response(serializer.data)
    if request.method == 'POST':
        error_message = "Make sure the title of the thread is unique"

        if request.user.is_authenticated:
            category_object = Category.objects.get(name__icontains = request.data['category'])
            del request.data['category']
            serializer = CreateThreadSerializer(data=request.data) 
            if serializer.is_valid():  
                instance = serializer.save() 
                instance.category = category_object
                instance.save()
            else: 
                #400 code
                return HttpResponse(status=400)   

            return Response(serializer.data)
        else:
            return HttpResponse(status=401)

@api_view(['GET', 'PUT', 'DELETE'])
def thread(request, id):
    if request.method == "GET":
        try:
            thread = Thread.objects.get(id=id)
        except:
            return HttpResponse(status=400)
        if not thread:
            return HttpResponse(status=400)
        serializer = ThreadSerializer(thread, many=False)
        return Response(serializer.data)
    if request.method == "PUT":
        error_message = "Make sure the the title of the thread is unique and has text"
        thread = Thread.objects.get(id=id)
        
        if request.user.is_authenticated:
            serializer = CreateThreadSerializer(instance=thread, data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                except IntegrityError as e: 
                    if 'UNIQUE constraint' in e.args[0]: return HttpResponse(status=400, content=error_message)   
                serializer.save()
            else: 
                return HttpResponse(status=400, content=error_message)   
            return Response(serializer.data)
        else:
            return HttpResponse(status=401)
    if request.method == 'DELETE':
        if request.user.is_authenticated and request.user.is_superuser:
            thread = Thread.objects.get(id=id)
            thread.delete()
        else:
            return HttpResponse('Not Admin')
    return Response('Item successfully deleted!')
    