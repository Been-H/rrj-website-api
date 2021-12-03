from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from django.core import serializers

from author_auth.models import AuthorUser
from author_auth.serializers import AuthorAccessSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from threads.models import Thread

@api_view(['GET'])
def author(request):
    print(request.user)
    if request.user.is_authenticated:
        author = request.user
        serializer = AuthorAccessSerializer(author, many=False)
        return Response(serializer.data)
    else:
        return HttpResponse(status=400)
    
    