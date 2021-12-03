from django.db import models
from author_auth.models import AuthorUser
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.TextField(max_length=20, unique=True)
    