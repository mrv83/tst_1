import os
from copy import deepcopy

from .base_conf import Base


class Local(Base):
    DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    COMPRESS_ENABLED = True

    INSTALLED_APPS = deepcopy(Base.INSTALLED_APPS) + [
        'django_extensions',
        'django_tools'
        ]

    DATABASES = {
        'default': {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "PORT": os.getenv("DB_PORT") or "5432",
            "USER": os.getenv("DB_USER") or "test_user",
            "PASSWORD": os.getenv("DB_PASSWORD") or "test_password",
            "HOST": os.getenv("DB_HOST") or "localhost",
            "NAME": os.getenv("DB_NAME") or "test_db",
        },
    }

    ALLOWED_HOSTS = ['*']

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'

    CORS_ORIGIN_WHITELIST = [
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ]
