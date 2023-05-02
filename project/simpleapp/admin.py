from django.contrib import admin
from .models import Category, Product, NewsPortal, NewsCategory   # импортируем категории(классы из models)

# Приложение с товарами
admin.site.register(Category)
admin.site.register(Product)

# Приложение с новостями
admin.site.register(NewsPortal)
admin.site.register(NewsCategory)
# Register your models here.
