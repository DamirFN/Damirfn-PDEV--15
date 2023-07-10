from django.contrib import admin
from .models import *    # импортируем категории(классы из models)

class NewsCategoryInline(admin.TabularInline):
    model = NewsPortalCategory
    extra = 1

def delete_all_chosen(modeladmin, request, queryset):
    queryset.delete()
    delete_all_chosen.short_description = 'Удалить все выбранные позиции'

class NewsPortalAdmin(admin.ModelAdmin):
    model = NewsPortal
    inlines = (NewsCategoryInline,)
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с новостями
    # list_display = [field.article_title for field in NewsPortal._meta.get_fields()]  # генерируем список имён всех
    # полей для более красивого отображения
    list_display = ('article_title', 'article_author', 'sort_date_of_publication')    # Отображение определенных
    # характеристик
    list_filter = ('article_title', 'article_author', 'sort_date_of_publication')  # Фильтры
    search_fields = ('article_title', 'category__article_title')  # Поиск
    actions = [delete_all_chosen]  # добавляем действия в список

# Приложение с новостями
admin.site.register(NewsCategory)
admin.site.register(NewsPortalCategory)
admin.site.register(NewsPortal, NewsPortalAdmin)
# admin.site.unregister(NewsPortal)   # разрегистрируем наши категории новостей

# Register your models here.
