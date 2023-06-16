from django.contrib import admin
from .models import *    # импортируем категории(классы из models)

# создаём новый класс для представления новостей в админке
class NewsAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с новостями
    list_display = [field.name for field in NewsPortal._meta.get_fields()]  # генерируем список имён всех
    # полей для более красивого отображения
    # list_display = ('article_title', 'article_author')

class NewsCategoryInline(admin.TabularInline):
    model = NewsPortalCategory
    extra = 1

class NewsPortalAdmin(admin.ModelAdmin):
    model = NewsPortal
    inlines = (NewsCategoryInline,)

# Приложение с новостями
admin.site.register(NewsCategory)
admin.site.register(NewsPortalCategory)
admin.site.register(NewsPortal, NewsPortalAdmin)
# admin.site.unregister(NewsPortal)   # разрегистрируем наши категории новостей

# Register your models here.
