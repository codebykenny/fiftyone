"""
Django settings for FiftyOne project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's)87pf6@q6xwro$*@nw_467^ds2x5l228824ly-m=kxsi3vvr3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

TEMPLATE_DIRS = (
    join(BASE_DIR,  'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

INSTALLED_APPS = (
    'wpadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'compressor'
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'FiftyOne.urls'

WSGI_APPLICATION = 'FiftyOne.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# COMPRESS_STORAGE = 'FiftyOne.CachedS3BotoStorage.CachedS3BotoStorage'

# AWS_ACCESS_KEY_ID = 'AKIAI6KGVLEEOVTOWODA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'fiftyone2'
# AWS_S3_SECURE_URLS = False
# AWS_QUERYSTRING_AUTH = False

# # STATIC_ROOT = 'staticfiles'
# COMPRESS_OUTPUT_DIR = 'compressed'
# COMPRESS_ROOT = 'static/compressed/'
# STATICFILES_STORAGE = COMPRESS_STORAGE

# STATIC_URL = "http://fiftyone2.s3-us-west-2.amazonaws.com/"
# COMPRESS_URL = STATIC_URL
# COMPRESS_ENABLED = True


# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '../static'),
# )

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
COMPRESS_URL = STATIC_URL

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

COMPRESS_ENABLED=True

WPADMIN = {
    'admin': {
        'title': 'Django admin panel',
        'menu': {
            'top': 'wpadmin.menu.menus.BasicTopMenu',
            'left': 'wpadmin.menu.menus.BasicLeftMenu',
        },
        'dashboard': {
            'breadcrumbs': True,
        },
        'custom_style': STATIC_URL + 'wpadmin/css/themes/sunrise.css',
    }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

COMPRESS_OFFLINE = True