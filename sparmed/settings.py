import os
BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..').replace('\\', '/')


DEBUG = False
TEMPLATE_DEBUG = DEBUG

HTTPS = False

ADMINS = (
  ('RamiAhmed', 'rami@alphastagestudios.com'),
)

MANAGERS = ADMINS

from django.utils.crypto import get_random_string
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# Django Sites ID
SITE_ID = 1

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.herokuapp.com').split(':')

from postgresify import postgresify
DATABASES = postgresify()

from memcacheify import memcacheify
CACHES = memcacheify()

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

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


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
  'compressor',
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
  'django.middleware.cache.UpdateCacheMiddleware',
  'htmlmin.middleware.HtmlMinifyMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.cache.FetchFromCacheMiddleware',
  'htmlmin.middleware.MarkRequestMiddleware',
)

# Mandrill email settings
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('MANDRILL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MANDRILL_APIKEY')
EMAIL_USE_TLS = True

SERVER_EMAIL = "SparMed.dk <info@SparMed.dk>"

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = "SparMed.dk"



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}