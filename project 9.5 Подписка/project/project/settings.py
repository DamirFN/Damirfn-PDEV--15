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
]



SITE_URL = 'http://127.0.0.1:8000/'

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Google-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'damirfn12345'   # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо
# писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = '*********'  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но
# включать его здесь обязательно
# здесь указываем уже свою ПОЛНУЮ почту, с которой будут отправляться письма
DEFAULT_FROM_EMAIL = 'damirfn12345@yandex.ru'

ADMINS = [
    ('damirdream', 'dreamstarsd@gmail.com'),
    ('12345damirfn', 'damirfn12345@yandex.ru'),
    ('damirfn', 'damirfn@mail.ru')
    # список всех админов в формате ('имя', 'их почта')
]
SERVER_EMAIL = 'damirfn12345@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

# Подключение allauth - модуль регистрации, логирования и логаут
ACCOUNT_EMAIL_REQUIRED = True    # поле email обязательное
ACCOUNT_UNIQUE_EMAIL = True      # уникальный email
ACCOUNT_USERNAME_REQUIRED = False    # пользователь не уникальный
ACCOUNT_AUTHENTICATION_METHOD = 'email'   # аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'none'     # верификация почты отсутствует

#Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию, необходимо добавить
# строчку в файл настроек проекта settings.py:
ACCOUNT_FORMS = {'signup': 'simpleapp.forms.CommonSignupForm'}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (css, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

#LOGIN_URL = 'templates/flatpages' переменная LOGIN_URL, то декоратор LoginRequiredMixin перенаправит пользователя
# на страницу входа. После успешного завершения входа на сайт, сайт будет перенаправлен обратно на то представление,
# для которого был вызван декоратор.

LOGIN_URL = '/accounts/login/'   # для allauth
LOGIN_REDIRECT_URL = '/profile/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']
