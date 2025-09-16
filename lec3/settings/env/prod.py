from base import * 
DEBUG = False
ALLOWED_HOSTS = ["localhost"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
}

SECRET_KEY = 'django-insecure-pe74w=p9ujmrs&o8-t0g#=k12wb175$d&pqwdw()nxsn!ba*3f'