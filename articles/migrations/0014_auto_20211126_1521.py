# Generated by Django 3.1.7 on 2021-11-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]