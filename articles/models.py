from django.db import models
from author_auth.models import AuthorUser
from ckeditor.fields import RichTextField
from category.models import Category
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images', null=True, blank=True),
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(AuthorUser, null=True, on_delete=models.SET_NULL)
    body = RichTextField(unique=False)
    posted = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    ready_for_edit = models.BooleanField(default=False)