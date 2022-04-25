from CourseStore.settings.base import *
import os

DEBUG = True

ALLOWED_HOSTS = ["course-store-x.herokuapp.com", "127.0.0.1"]

SECRET_KEY = os.environ.get("PROD_SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("PROD_DB_ENGINE"),
        "NAME": os.environ.get("PROD_DB_NAME"),
        "USER": os.environ.get("PROD_DB_USER"),
        "PASSWORD": os.environ.get("PROD_DB_PS"),
        "HOST": os.environ.get("PROD_DB_HOST"),
        "PORT": os.environ.get("PROD_DB_PORT"),
    }
}


AWS_ACCESS_KEY_ID = os.environ.get("CS_S3_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("CS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("CS_S3_BUCKET_NAME")

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_HOST = "s3.us-east-2.amazonaws.com"
AWS_S3_REGION_NAME = "us-east-2"

AWS_QUERYSTRING_AUTH = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True