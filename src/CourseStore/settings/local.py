from CourseStore.settings.base import *


DEBUG = True

SECRET_KEY = 'django-insecure-&pv8@!ethev)po&9!%vd3ppgs0k-!uof2#)8r_yn1l1zl41rao'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}