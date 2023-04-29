from django.contrib import admin
from .models import Category, Product   # ипортируем категории(классы из models)

admin.site.register(Category)
admin.site.register(Product)
# Register your models here.
