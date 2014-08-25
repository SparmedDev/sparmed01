"""
Django settings for sparmed project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..').replace('\\', '/')


DEBUG = True
TEMPLATE_DEBUG = DEBUG

HTTPS = False

ADMINS = (
  ('RamiAhmed', 'rami@alphastagestudios.com'),
)

MANAGERS = ADMINS

# Django Sites ID
SITE_ID = 1

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.herokuapp.com').split(':')

from postgresify import postgresify
DATABASES = postgresify()

#from memcacheify import memcacheify
#CACHES = memcacheify()

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = True
USE_TZ = True

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'mediafiles')
MEDIA_URL = STATIC_URL + 'media/'

from django.utils.crypto import get_random_string
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))


TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.request',
  'django.contrib.auth.context_processors.auth',
  'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'sparmed.urls'

WSGI_APPLICATION = 'sparmed.wsgi.application'

# Grappelli Admin Site Settings
GRAPPELLI_ADMIN_TITLE = "Admin | Sparmed.dk"


GRAPPELLI = (
  'grappelli',
)

DJANGO_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.messages',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.sitemaps',
  'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
  'gunicorn',
  #'compressor',
  #'analytical',
  #'jquery',
  'bootstrap3',
  #'disqus',
  #'embed_video',
  #'taggit',
  #'robots',
  #'storages',
  #'wysihtml5',
  #'collectfast',
)

LOCAL_APPS = (
  'sparmed',
)

INSTALLED_APPS = GRAPPELLI + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
