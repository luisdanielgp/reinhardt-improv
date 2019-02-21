import os

from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
KEY_DIRS = os.path.join(BASE_DIR, 'settings/keys')

with open(KEY_DIRS + '/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'reinhardt_postgres',
        'PORT': '5432',
    }
}

# Configuration for whitenoise
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/assets/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
