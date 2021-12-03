from django.db import models
from articles.models import Article
from author_auth.models import AuthorUser
from django.utils import timezone
from category.models import Category

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(AuthorUser, null=True, on_delete=models.SET_NULL, related_name='+')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    articles = models.ManyToManyField(Article, null=True)
    authors = models.ManyToManyField(AuthorUser, null=True)
    date_created = models.DateTimeField(default=timezone.now)
