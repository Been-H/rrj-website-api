# Generated by Django 3.1.7 on 2021-11-26 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20211126_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]