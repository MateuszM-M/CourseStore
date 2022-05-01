from CourseStore.settings.base import *
import os

DEBUG = True

ALLOWED_HOSTS = ["herokuapp.com", "127.0.0.1"]

SECRET_KEY = os.environ.get("DEV_SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DEV_DB_ENGINE"),
        "NAME": os.environ.get("DEV_DB_NAME"),
        "USER": os.environ.get("DEV_DB_USER"),
        "PASSWORD": os.environ.get("DEV_DB_PS"),
        "HOST": os.environ.get("DEV_DB_HOST"),
        "PORT": os.environ.get("DEV_DB_PORT"),
    }
}