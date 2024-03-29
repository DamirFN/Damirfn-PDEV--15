"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
# import logging
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)$*vmz!5k39jqoh&8h1ap%yx@&h5c$3!rhx1ish$@pu9873b+r'

# SECURITY WARNING: don't run with a debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # - '*' Доступ ко всем хостам

# Application definition

INSTALLED_APPS = [
    'modeltranslation',  # обязательно впишите его перед админом

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'django.contrib.sites',

    'django.contrib.flatpages',
    'fpages',

    'simpleapp.apps.SimpleappConfig',
    'django_filters',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'django_apscheduler',
]

SITE_URL = 'http://127.0.0.1:8000'  # Для отправки сигналов при появлении новой статьи или новости

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Google-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'damirfn12345'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо
# писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = '*********'  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но
# включать его здесь обязательно
# здесь указываем уже свою ПОЛНУЮ почту, с которой будут отправляться письма
DEFAULT_FROM_EMAIL = 'damirfn12345@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

ADMINS = [
    ('damirdream', 'dreamstarsd@gmail.com'),
    ('12345damirfn', 'damirfn12345@yandex.ru'),
    ('damirfn', 'damirfn@mail.ru')
    # список всех админов в формате ('имя', 'их почта')
]
SERVER_EMAIL = 'damirfn12345@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

# Подключение allauth - модуль регистрации, логирования и логаут
ACCOUNT_EMAIL_REQUIRED = True  # поле email обязательное
ACCOUNT_UNIQUE_EMAIL = True  # уникальный email
ACCOUNT_USERNAME_REQUIRED = False  # пользователь не уникальный
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'none'  # mandatory верификация почты отсутствует

# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию, необходимо добавить
# строчку в файл настроек проекта settings.py:
ACCOUNT_FORMS = {'signup': 'simpleapp.forms.CommonSignupForm'}

SITE_ID = 1

CELERY_BROKER_URL = 'redis://default:QqT6z8XsLUIRKIf8KSdaeU6fvFsLJxGO@redis-19198.c258.us-east-1-4.ec2.cloud.redislabs.com:19198'
# Указывает на URL брокера сообщений (Redis). По умолчанию он находится на порту 6379.
CELERY_RESULT_BACKEND = 'redis://default:QqT6z8XsLUIRKIf8KSdaeU6fvFsLJxGO@redis-19198.c258.us-east-1-4.ec2.cloud.redislabs.com:19198'
# указывает на хранилище результатов выполнения задач.

CELERY_ACCEPT_CONTENT = ['application/json']   # допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json'    # метод сериализации задач.
CELERY_RESULT_SERIALIZER = 'json'   # метод сериализации результатов.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),  # Указываем, куда будем сохранять кэшируемые файлы! Не
        # забываем создать папку cache_files внутри папки с manage.py!
        # 'TIMEOUT': 300,  # добавляем стандартное время ожидания в минуту (по умолчанию это 5 минут — 300 секунд)
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Пожалуй, один из главных промежуточных слоев, потому что он
    # реализует различные проверки безопасности — XSS, nosniff, HSTS, CORS, поддержка SSL и т. д.

    'django.contrib.sessions.middleware.SessionMiddleware',  # Включает механизм сессий в разрабатываемом приложении.

    'django.middleware.common.CommonMiddleware',  # Рекомендуемый для использования во всех Django-проектах, потому что
    # он позволяет выполнять стандартные процедуры над URL

    'django.middleware.csrf.CsrfViewMiddleware',  # Включает проверку безопасности от угроз типа CSRF.

    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Реализует основы аутентификации и идентификации.

    'django.contrib.messages.middleware.MessageMiddleware',  # Включает поддержку сообщений, лежащих в основе работы с
    # куки и сессиями.

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',  # активация статических страничек

    'django.middleware.locale.LocaleMiddleware',  # Локализация интернационализации
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Подключение allauth - модуль регистрации, логирования и логаута
# pip install django-allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`.
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail.
    'allauth.account.auth_backends.AuthenticationBackend'
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

# LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

TIME_ZONE = 'UTC'

USE_I18N = True   # интернационализации будут поддерживаться в нашем приложении

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]   # Для активации gettext-utils в Programm Files и активации интернационализации

# Static files (css, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# LOGIN_URL = 'templates/flatpages' переменная LOGIN_URL, то декоратор LoginRequiredMixin перенаправит пользователя
# на страницу входа. После успешного завершения входа на сайт, сайт будет перенаправлен обратно на то представление,
# для которого был вызван декоратор.

LOGIN_URL = '/accounts/login/'  # для allauth
LOGIN_REDIRECT_URL = '/profile/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#             "filters": ["console_only"],
#         },
#         "general_file": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": "logs/general.log",
#             "maxBytes": 1048576,  # 1MB
#             "backupCount": 10,
#             "formatter": "simple",
#             "filters": ["email_file_only"],
#         },
#         "errors_file": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": "logs/errors.log",
#             "maxBytes": 1048576,  # 1MB
#             "backupCount": 10,
#             "formatter": "verbose",
#             "filters": ["email_file_only"],
#         },
#         "security_file": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": "logs/security.log",
#             "maxBytes": 1048576,  # 1MB
#             "backupCount": 10,
#             "formatter": "verbose",
#             "filters": ["email_file_only"],
#         },
#         "mail_admins": {
#             "class": "django.utils.log.AdminEmailHandler",
#             "include_html": True,
#             "filters": ["email_file_only"],
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console", "general_file"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "django.request": {
#             "handlers": ["errors_file", "mail_admins"],
#             "level": "ERROR",
#             "propagate": False,
#         },
#         "django.server": {
#             "handlers": ["errors_file", "mail_admins"],
#             "level": "ERROR",
#             "propagate": False,
#         },
#         "django.template": {
#             "handlers": ["errors_file"],
#             "level": "ERROR",
#             "propagate": False,
#         },
#         "django.db.backends": {
#             "handlers": ["errors_file"],
#             "level": "ERROR",
#             "propagate": False,
#         },
#         "django.security": {
#             "handlers": ["security_file"],
#             "level": "DEBUG",
#             "propagate": False,
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "DEBUG",
#     },
#     "filters": {
#         "console_only": {
#             "()": "django.utils.log.CallbackFilter",
#             "callback": lambda record: settings.DEBUG,
#         },
#         "email_file_only": {
#             "()": "django.utils.log.CallbackFilter",
#             "callback": lambda record: not settings.DEBUG,
#         },
#     },
#     "formatters": {
#         "verbose": {
#             "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#         },
#         "simple": {
#             "format": "%(asctime)s %(levelname)s [%(module)s] %(message)s",
#         },
#     },
# }
