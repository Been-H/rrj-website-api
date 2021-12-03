from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=60)
    body = models.TextField()
    posted=models.BooleanField(default=False)