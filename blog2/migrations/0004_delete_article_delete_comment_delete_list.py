# Generated by Django 5.2 on 2025-04-12 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0003_article_comment_list'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
