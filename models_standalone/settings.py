import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '69lsidk6+1&4y7p2xs=_5@7_qgx!na)=s1ob0g-+t%a6lvrc^a'

# WARNING: when DEBUG is True, don't forget to reset db connection to avoid memory leaks in your standalone app!
DEBUG = True

INSTALLED_APPS = (
        "models_standalone",
)

MIDDLEWARE_CLASSES = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'aws': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgresqlNowtufy',
        'USER': 'teamgemini',
        'PASSWORD': 'n0wtify123',
        'HOST': 'postgresql-nowtify.c45gsg3njvop.ap-southeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
