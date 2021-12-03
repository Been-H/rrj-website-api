from rest_framework import serializers

from category.models import Category
from .models import Thread
from articles.serializers import ArticleSerializer
from author_auth.models import AuthorUser
from author_auth.serializers import AuthorAccessSerializer
from category.serializers import CreatCategorySerializer

class CreateThreadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Thread
        fields = ['title'] 

class ThreadSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format="%m/%d/%Y")
    articles = ArticleSerializer(read_only=True, many=True)
    authors = AuthorAccessSerializer(read_only=True, many=True)
    category = serializers.SerializerMethodField('get_category_name')

    class Meta:
        model = Thread
        fields = ['title', 'id', 'date_created', 'category', 'articles', 'authors'] 
        
    def get_category_name(self, thread):
        if not thread.category:
            return "No Category"
        name = thread.category.name
        return name


# def __init__(self, data):
#         category_object = Category.objects.get(name__icontains = data['category'])
#         self.category = category_object