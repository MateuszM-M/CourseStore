from CourseStore.settings.base import *
import os

DEBUG = True

SECRET_KEY = 'django-insecure-&pv8@!ethev)po&9!%vd3ppgs0k-!uof2#)8r_yn1l1zl41rao'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": 'db',
        "PORT": "5432"
    }
}
