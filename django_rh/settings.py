# -*- coding: utf-8 -*-
from unipath import Path
import djcelery


djcelery.setup_loader()

PROJECT_DIR = Path(__file__).parent

BROKER_URL = 'django://'

DEFAULT_FROM_EMAIL = 'Contato <contato@xpto.com.br>'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = True

ADMINS = (
    ('Jeferson Farias Calazans', 'calazans10@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rh_system',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_DIR.child('media')

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_DIR.child('static_root')

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"
STATICFILES_DIRS = (PROJECT_DIR.child('static'),)
TEMPLATE_DIRS = (PROJECT_DIR.child('templates'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '^z4(*0w(k-rx^0sn5ed8aib9$dbn0z3xu2r6u_^@%ct^wl7ul5'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'emailusernames.backends.EmailAuthBackend',
)


ROOT_URLCONF = 'django_rh.urls'

WSGI_APPLICATION = 'django_rh.wsgi.application'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'south',
    'djcelery',
    'ajax_select',
    'emailusernames',
    'kombu.transport.django',
    'django_extensions',

    'employees',
)

AJAX_LOOKUP_CHANNELS = {
    'user': {'model': 'auth.user', 'search_field': 'email'},
}

AJAX_SELECT_BOOTSTRAP = True
AJAX_SELECT_INLINES = 'inline'

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
