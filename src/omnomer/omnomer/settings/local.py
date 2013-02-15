# Local settings
from .base import *

DEBUG = True
TEAMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINGE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'omnomer',
		'USER': '',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '',
	}
}

INSTALLED_APPS += ('debug_toolbar', )
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += \
            ('debug_toolbar.middleware.DebugToolbarMiddleware', )