from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db import IntegrityError
from .models import AuthorUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import token_blacklist
from .serializers import AuthorUserCreationSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def author_auth(request):
    if request.method == 'GET':
        requires_superuser = request.query_params['req-supuser']
        if requires_superuser == "True":
            requires_superuser = True
        else:
            requires_superuser = False
        if request.user.is_authenticated:
            if requires_superuser == True:
                if request.user.is_superuser:
                    return Response('Authenticated')
                return HttpResponse('Not Admin')
            return Response('Authenticated') 
        return HttpResponse(status=401)
        
    if request.method == 'POST' and request.user.is_superuser:
        
        error_message = "Make sure the email and name are not already in use and that the password is strong"
        create_serializer = AuthorUserCreationSerializer(data=request.data)
        
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

class BlackListToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)