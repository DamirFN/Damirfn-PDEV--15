"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the included() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # подключаем встроенные эндопинты для работы с локализацией
    path('admin/', admin.site.urls),   # страница админа
    path('pages/', include('django.contrib.flatpages.urls')),    # путь нахождение все страниц проекта

    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
    # подключались к главному приложению с префиксом news/.
    #path('news/', include('simpleapp.urls')),


    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
    # подключались к главному приложению с префиксом products/.
    # path('products/', include('simpleapp.urls'))

    path('', include('simpleapp.urls')),    # если нам нужно создавать статью и новость отдельно, универсальный
    # путь http://127.0.0.1:8000/''

    # Подключение allauth - модуль регистрации, логирования и логаут
    path('accounts/', include('allauth.urls')),
]
