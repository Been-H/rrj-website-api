from rest_framework import serializers
from .models import Category

class CreatCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name'] 
        
