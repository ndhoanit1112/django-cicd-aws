try:
    from app.settings_base import *
except ImportError:
    pass

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

from kombu.utils.url import safequote

aws_access_key = safequote(env('AWS_SQS_ACCESS_KEY_ID'))
aws_secret_key = safequote(env('AWS_SQS_SECRET_ACCESS_KEY'))

CELERY_BROKER_URL = "sqs://{aws_access_key}:{aws_secret_key}@".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "region": env("AWS_SQS_REGION"),
    'queue_name_prefix': 'django-deploy-',
    'visibility_timeout': 7200,
    'polling_interval': 1
}
