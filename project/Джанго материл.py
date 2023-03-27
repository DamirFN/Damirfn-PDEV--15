# Основные команды создания проекта на Django
# python -m venv venv - создание виртуального окружения

# python -m venv venv создаёт в текущей директории виртуальное окружение с именем
# SkillFactory

# venv\scripts\activate - активируем виртуальное окружение
# pip list - проверка установленных пакетов в окружении

# pip install django - устанавливаем Django

#--------------------------------------------------------------------------------
# django-admin startproject project - создаем пустой проект Django

# cd project - переходим в папку с проектом

# python manage.py runserver - запускаем пустой проект

# Это сообщение говорит нам о том, что приложение начало работу по адресу
# 127.0.0.1:8000. вместо 127.0.0.1 можно прописать localhost И то, и то указывает
# на адрес локальной машины, где у нас и крутится наш собственны Django-сервер.

# Останавливаем сервер командой fn + B(ctrl+Break) fn ctrl+B, ctrl+C

# python manager.py migrate - запускаем миграцию т.е. применяем все приложения из
# settings из списка INSTALLED_APPS

# python manager.py createsuperuser - создаем admina

# python manager.py runserver - запускаем сервер и проходим по адресу

# к адресу добаляем /admin - и авторизуемся. За авторизаци и индетификацию на
# сервере страницы отвечает urls.py, urlpatterns = [path('admin/', admin.site.urls),]

# за группу AUTHENTICATION AND AUTHORIZATION отвечает settings, INSTALLED_APPS,
# django.contrib.auth

# в user, dream, in this form - можно поменять пароль

#--------------------------------------------------------------------------------
# Создаем статичные страницы:

# останавливаем сервер
# вносим(подключаем) в settings, INSTALLED_APPS: django.contrib.sites и
# django.contrib.flatpages
# добавляем переменную туда же ниже, SITE_ID = 1 - идентификатор сайта, который
# представляет файл настроек
# Добавьте запись в свой URLconf. Например:
# urlpatterns = [
#     path('pages/', include('django.contrib.flatpages.urls')),
# ]
# Добавьте 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware' в свою
# MIDDLEWARE настройку.Запустите команду .manage.py migrate
# запускаем сервер и в Django administration заходим во вкладку Flat pages +ADD
# там прописываем стандартный URL /about/
# в title прописываем название статичной страницы
# в Content прописываем текст, можно <h1>Hallo Damir!</h1> или <h2>Wie geht es dir?</h2>
# Sites стандартное example.com
# можно добавить расширенные настрой advanced
# что бы не вышла ошибка по адресу статичной страницы:
# http://127.0.0.1:8000/about/, нужно создать шаблон страницы с адресом и
# стандартными html, а именно в папке проект создаем папку templates в ней папку
# flatpages, а в ней файл default.html с текстом:

# <!DOCTYPE html>
# <html>
# <head>
# <title>{{ flatpage.title }}</title>
# </head>
# <body>
# {{ flatpage.content }}
# </body>
# </html>

# где специальной разметкой {{ flatpage.title }} ставим название страницы с
# настроек Flat pages на странице Django administration, так же можно вместо
# разметки свой тексе, он заменит администраторский.
# далее в setting.py в настройке TEMPLATES в ключе 'DIRS' прописываем путь для
# считывания нашего шаблона с default или своим файл. Для этого пишем путь:
# 'DIRS': [os.path.join(BASE_DIR, 'templates')], импортируем так же import os!!!

#--------------------------------------------------------------------------------
# Создаем настройки во Django administration, Flat pages -
# Enable comments (разрешить комментировать) и Registration required
# (смотреть страницу только зарегистрированным пользователям)
# Создаем файл перенастройки админа по пути project/fpages/admin.pyс кодом
# внутри:
# from django.contrib import admin
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# from django.utils.translation import gettext_lazy as _

# Define a new FlatPageAdmin(Определите нового администратора плоской страницы)
# class FlatPageAdmin(FlatPageAdmin):
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites')}),
#         (_('Advanced options'), {
#             'classes': ('collapse',),
#             'fields': (
#                 'enable_comments',
#                 'registration_required',
#                 'template_name',
#             ),
#         }),
#     )
#
#
# # Re-register FlatPageAdmin(перенастройка админа)
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)

# в INSTALLED_APPS прописываем новое приложение 'fpages'

#--------------------------------------------------------------------------------
# ALLOWED_HOSTS = ['*'] # - '*' Доступ ко всем хостам, выставляется в
# settings

#--------------------------------------------------------------------------------
# Наследования шаблонов
# это наследование content, title из одной flatpage в другую

# templates/flatpages/default.html (наследник)
#
# <!DOCTYPE html>
# <html>
# <head>
# <title>{{ flatpage.title }}</title>
# </head>
# <body>
# {% include 'flatpages/contact_page.html' %}
# </body>
# </html>

# templates/flatpages/contact_page.html (родитель)

#--------------------------------------------------------------------------------
# Bootstrap — это библиотека для упрощения работы с HTML- и CSS-кодом.
# В ней готовые шаблоны страниц
# После того как мы скачаем архив с готовыми шаблонами CSS-файлами и т. д., нам надо
# распаковать его в директорию static/ (папку static надо будет создать самостоятельно
# в той же папке, что и manage.py). Из всего нам потребуется только файл index.html и
# папка css, в которой как раз-таки будут лежать наши стили. assets и js можно
# спокойно удалить, они нам пока не понадобятся. В assets лежит иконка, а в
# js — пустой скрипт (так как наша страница статична).
# И в настройках добавить строчку в самом конце, для подгрузки стилей из папки static:
# STATICFILES_DIRS = [BASE_DIR / "static"]

# {% load static %}
#
# <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
#
# <link href="css/styles.css" rel="stylesheet" />  на
# <link href="{% static 'css/styles.css' %}" rel="stylesheet" />



# Сайт с программой для создания тунельного соединения для демонстрации своих веб
# приложений
# https://dashboard.ngrok.com/get-started/setup