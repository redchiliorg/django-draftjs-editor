import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

SECRET_KEY = 'test'

INSTALLED_APPS = (
    'draftjs_editor',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'draftjs_editor',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DRAFTJS_EDITOR_UPDATE_SNAPSHOTS = 'UPDATE_SNAPSHOTS' in os.environ
