from CourseStore.settings.base import *
import os

DEBUG = False

ALLOWED_HOSTS = ["herokuapp.com", "127.0.0.1"]

SECRET_KEY = os.environ.get("DEV_SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": 'db',
        "PORT": "5432"
    }
}