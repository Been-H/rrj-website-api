from copy import Error
from django.db.utils import InternalError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from django.core import serializers
from django.db import IntegrityError

from .models import Category
from threads.models import Thread
from author_auth.models import AuthorUser
from .serializers import CreatCategorySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response 


@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CreatCategorySerializer(categories, many=True)
        return Response(serializer.data)
    if request.method == 'POST' and request.user.is_superuser:
        
        error_message = "Make sure the category name is unique"
        create_serializer = CreatCategorySerializer(data=request.data)
        
        if create_serializer.is_valid():
            try:
                create_serializer.save()
            except IntegrityError as e: 
                if 'UNIQUE constraint' in e.args[0]:
                    return HttpResponse(status=400, content=error_message)   
        else:
            return HttpResponse(status=400, content=error_message)
        
        return Response(create_serializer.data)
    else:
        return HttpResponse('Not Admin')

@api_view(['DELETE'])
def category(request, name):
    if request.method == 'DELETE':
        if request.user.is_authenticated and request.user.is_superuser:
            category = Category.objects.get(name__icontains = name)
            category.delete()
        else:
            return HttpResponse('Not Admin')
    return Response('Item successfully deleted!')