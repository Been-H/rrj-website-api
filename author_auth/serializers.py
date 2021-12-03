from rest_framework import serializers
from .models import AuthorUser
from threads.models import Thread

class AuthorUserCreationSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    is_superuser = serializers.BooleanField(default=False)

    class Meta:
        model = AuthorUser
        fields = ('email', 'name', 'password', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    
    # def error_handle(self, data):
    #     try 

class AuthorAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorUser
        fields = ('name', 'date_joined', 'bio')