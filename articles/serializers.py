from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Article
from author_auth.models import AuthorUser

class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField('get_author_name')
    category_name = serializers.SerializerMethodField('get_category_name')
    date_created = serializers.DateTimeField(format="%m/%d/%Y")
    # image = SerializerMethodField('get_image_link')

    class Meta:
        model = Article
        fields = ['title', 'id', 'body', 'author_name', 'category_name', 'posted', 'date_created'] 
    
    def get_author_name(self, article):
        if not article.author:
            return "Author Deleted"
        name = article.author.name
        return name

    def get_category_name(self, article):
        if not article.category:
            return "No Category"
        name = article.category.name
        return name
    
    def get_image_link(self, article):
        print('127.0.0.1:8000/' + str(article.image))
    
    # def create(self, validated_data):
    #     author_id = validated_data.pop('author', None)
    #     instance = self.Meta.model(**validated_data)
    #     if author_id is not None:
    #         instance.author = AuthorUser.objects.get(id=author_id)
    #     instance.save()
    #     return instance

class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'body'] 


class ArticleUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ['title', 'body']


# class ArticleGetSerializer(serializers.ModelSerializer):
#     author_name = serializers.SerializerMethodField('get_author_name')

#     class Meta:
#         model = Article
#         fields = ['title', 'body', 'author_name'] 

#     def get_author_name(self, article):
#         name = article.author.name
#         return name