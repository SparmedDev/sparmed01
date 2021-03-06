import os
BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..').replace('\\', '/')

# Current domain
DOMAIN_NAME = os.environ.get('DOMAIN_NAME', '.sparmed.dk')

# Debug settings
DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
TEMPLATE_DEBUG = DEBUG
HTTPS = False

# Security # Enable for  HTTPS
SECURE_SSL_REDIRECT = HTTPS
SECURE_HSTS_SECONDS = 60 * 60  # 1 hour
SECURE_HSTS_INCLUDE_SUBDOMAINS = HTTPS
SECURE_FRAME_DENY = HTTPS
SECURE_CONTENT_TYPE_NOSNIFF = HTTPS
SECURE_BROWSER_XSS_FILTER = HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = HTTPS

SESSION_COOKIE_AGE = 62000
SESSION_SAVE_EVERY_REQUEST = True

# Admins
ADMINS = (
  ('RamiAhmed', 'rami@alphastagestudios.com'),
)

MANAGERS = ADMINS

AUTHENTICATION_BACKENDS = (
#    'auth.authentication.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Secret key
from django.utils.crypto import get_random_string
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# Django Sites ID
SITE_ID = 1

# Allowed hosts
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.herokuapp.com').split(':')

# Postgres database
from postgresify import postgresify
DATABASES = postgresify()

# Memcache Cache
from memcacheify import memcacheify
CACHES = memcacheify()
MEMCACHEIFY_USE_LOCAL=DEBUG

# The maximum number of entries allowed in the cache before old values are deleted. This argument defaults to 300.
MAX_ENTRIES = 200

ROOT_URLCONF = 'sparmed.urls'
WSGI_APPLICATION = 'sparmed.wsgi.application'

# Grappelli Admin Site Settings
GRAPPELLI_ADMIN_TITLE = "Admin | SparMED.dk"

THIRD_PARTY_PRE_DJANGO = (
  'grappelli',
  'grappelli_modeltranslation',
  'modeltranslation',
  'collectfast',
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
  'django.contrib.humanize',
)

THIRD_PARTY_APPS = (
  'gunicorn',
  'rosetta',
  'storages',
  'haystack',
  'bootstrap3',
  'robots',
  'sorl.thumbnail',
  'django_countries',
  'validatedfile',
  'colorfield',
  'cookielaw',
  'ckeditor',
  'nocaptcha_recaptcha',
)

LOCAL_APPS = (
  'sparmed',
  'cart',
  'contact',
  'shop',
  'news',
  'online_order',
  'certificates',
  'distributors',
  'economic',
  'index_page',
)

INSTALLED_APPS = THIRD_PARTY_PRE_DJANGO + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
  'django.middleware.cache.UpdateCacheMiddleware',
  'django.middleware.http.ConditionalGetMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.cache.FetchFromCacheMiddleware',
)

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
USE_TZ = True
FIRST_DAY_OF_WEEK = 1 # start week on Monday

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
  ('en', _('English')),
  ('ru', _('Russian')),
  ('pt-br', _('Brazilian')),
  ('es', _('Spanish')),
)

COMPLETED_LANGUAGES = (
  'en',
  #'ru',
  #'pt-br',
  #'es',
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_GOOGLE_TRANSLATE = False
YANDEX_TRANSLATE_KEY = os.environ.get('YANDEX_TRANSLATE_KEY')
ROSETTA_EXCLUDED_APPLICATIONS = THIRD_PARTY_PRE_DJANGO + DJANGO_APPS + THIRD_PARTY_APPS
ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage'

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

if not DEBUG:
    # Thumbnail Fix for S3 Slow Response
    THUMBNAIL_FORCE_OVERWRITE = True

    # Fix admin login cookie not being set correctly
    SESSION_COOKIE_DOMAIN = DOMAIN_NAME
    CSRF_COOKIE_DOMAIN = DOMAIN_NAME

    # Amazon AWS S3 credientials
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

    STATIC_ROOT = STATIC_URL
    MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
    MEDIA_UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')

    MEDIA_URL = STATIC_URL + 'media/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    from datetime import date, timedelta
    yearfromtoday = date.today() + timedelta(days=365)
    AWS_HEADERS = {
      'Cache-Control': 'public, max-age=86400',
      'Expires': yearfromtoday.strftime('%a, %d %b %Y 20:00:00 GMT'),
    }

    AWS_AUTO_CREATE_BUCKET = True
    AWS_S3_FILE_OVERWRITE = True
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_SECURE_URLS = True
    AWS_REDUCED_REDUNDANCY = False
    AWS_IS_GZIPPED = False
    AWS_PRELOAD_METADATA = True

    TEMPLATE_MINIFIER = True
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates')
                # insert your TEMPLATE_DIRS here
            ],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                    'cart.context_processors.get_cart',
                ],
                'loaders': [
                    ('django.template.loaders.cached.Loader', (
                        'template_minifier.template.loaders.filesystem.Loader',
                        'template_minifier.template.loaders.app_directories.Loader',
                    )),
                ]
            },
        },
    ]
else:
    COLLECTFAST_ENABLED = False

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

    STATIC_ROOT = PROJECT_ROOT + "/staticfiles/"
    STATIC_URL = STATIC_ROOT
    MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
    MEDIA_UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')

    MEDIA_URL = STATIC_URL + 'media/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates')
                # insert your TEMPLATE_DIRS here
            ],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                    'cart.context_processors.get_cart',
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]
            },
        },
    ]

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# SendGrid email settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SERVER_EMAIL = "SparMED.dk <info@SparMED.dk>"
DEFAULT_FROM_EMAIL = SERVER_EMAIL
EMAIL_SUBJECT_PREFIX = "SparMED.dk"

# Robots caching
ROBOTS_CACHE_TIMEOUT = 60*60*24 # = 24 hours

# LOGIN
LOGIN_REDIRECT_URL = '/distributor-login/'
LOGIN_URL = 'django.contrib.auth.views.login'

# Custom user model
AUTH_USER_MODEL = "online_order.SparmedUser"

# Required settings:
NORECAPTCHA_SITE_KEY = "6Leu_wITAAAAAJ2D3Hu1FqIjL61FhQaAxusckJHd"
NORECAPTCHA_SECRET_KEY = "6Leu_wITAAAAAJWZFk8DZMMjATryJh3Z0Yp_SDie"

# Optional Settings:
NORECAPTCHA_VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'
#    Best to leave this as the default setting.
#    Default is https://www.google.com/recaptcha/api/siteverify
NORECAPTCHA_WIDGET_TEMPLATE = 'nocaptcha_recaptcha/widget.html'
#    Default is nocaptcha_recaptcha/widget.html

# Haystack Settings
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

from urlparse import urlparse
es = urlparse(os.environ.get('SEARCHBOX_URL') or 'http://127.0.0.1:9200/')

es_port = es.port or 80

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'sparmed.search_backends.CustomElasticSearchEngine',
        #'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': es.scheme + '://' + es.hostname + ':' + str(es_port),
        'INDEX_NAME': 'haystack',
    },
}

if es.username:
    HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}

ELASTICSEARCH_INDEX_SETTINGS = {
    'settings': {
        "analysis": {
            "analyzer": {
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "lowercase",
                    "filter": ["haystack_ngram"]
                },
                "edgengram_analyzer": {
                    "type": "custom",
                    "tokenizer": "lowercase",
                    "filter": ["haystack_edgengram"]
                },
                "suggest_analyzer": {
                    "type":"custom",
                    "tokenizer":"standard",
                    "filter":[
                        "standard",
                        "lowercase",
                        "asciifolding"
                    ]
                },
            },
            "tokenizer": {
                "haystack_ngram_tokenizer": {
                    "type": "nGram",
                    "min_gram": 3,
                    "max_gram": 15,
                },
                "haystack_edgengram_tokenizer": {
                    "type": "edgeNGram",
                    "min_gram": 2,
                    "max_gram": 15,
                    "side": "front"
                }
            },
            "filter": {
                "haystack_ngram": {
                    "type": "nGram",
                    "min_gram": 3,
                    "max_gram": 15
                },
                "haystack_edgengram": {
                    "type": "edgeNGram",
                    "min_gram": 2,
                    "max_gram": 15
                }
            }
        }
    }
}

# CKEditor
CKEDITOR_JQUERY_URL = '//code.jquery.com/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Full': [
            [ 'Source','-', 'Preview','-', 'Print'],
            [ 'FontSize', '-', 'Format', '-', 'Bold', 'Italic', 'Underline', 'Strike', '-', 'Undo', 'Redo' ],
            [ 'Cut','Copy','Paste', '-', 'PasteText','PasteFromWord' ],
            [ 'Find','Replace','-','SelectAll'],
            [ 'NumberedList','BulletedList','-','Outdent','Indent',],
            [ 'JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            [ 'Link','Unlink' ],
            [ 'TextColor','BGColor' ],
        ],
        'toolbar': 'Full',
    },
}

# Logging
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
            'class': 'django.utils.log.AdminEmailHandler',
        },
        "console": {
            'level':'INFO',
            'class':'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        "django": {
            "handlers": ["console"],
            'level': 'INFO',
        },
        'elasticsearch': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}