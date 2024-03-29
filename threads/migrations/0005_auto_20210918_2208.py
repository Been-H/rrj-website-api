# Generated by Django 3.1.7 on 2021-09-19 02:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210917_2052'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0004_auto_20210918_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='articles',
            field=models.ManyToManyField(related_name='_thread_articles_+', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='authors',
            field=models.ManyToManyField(related_name='_thread_authors_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
