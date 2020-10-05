from .settings import *


DEBUG = True
THUMBNAIL_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:', # os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 30,
        }
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
