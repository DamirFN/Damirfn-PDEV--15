# Generated by Django 4.1.7 on 2023-07-16 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0003_remove_newscategory_subscribers_en_us_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsportalcategory_ru',
            name='news_category',
        ),
        migrations.RemoveField(
            model_name='newsportalcategory_ru',
            name='news_portal',
        ),
        migrations.RemoveField(
            model_name='newsportal',
            name='news_category_en_us',
        ),
        migrations.RemoveField(
            model_name='newsportal',
            name='news_category_ru',
        ),
        migrations.DeleteModel(
            name='NewsPortalCategory_en_us',
        ),
        migrations.DeleteModel(
            name='NewsPortalCategory_ru',
        ),
    ]
