from .models import NewsCategory, NewsPortal
from modeltranslation.translator import register, \
    TranslationOptions  # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться


# регистрируем наши модели для перевода

@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('article_title',)


@register(NewsPortal)
class NewsPortalTranslationOptions(TranslationOptions):
    fields = ('article_title', 'article_author', 'article_description',)
