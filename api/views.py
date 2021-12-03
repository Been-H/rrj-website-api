from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def api_overview(request):
    api_urls = {
            'Threads' : '/threads/',
            'Articles' : '/articles/',
            'Authors' : '/authors',
            'Auth' : '/auth/',
		}

    return Response(api_urls)

