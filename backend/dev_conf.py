import os

ALLOWED_HOSTS = ['*']
COMPRESS_ENABLED = False

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME") or "test_db",
        "USER": os.getenv("DB_USER") or "test_user",
        "PASSWORD": os.getenv("DB_PASSWORD") or "test_password",
        "HOST": os.getenv("DB_HOST") or "localhost",
        "PORT": os.getenv("DB_PORT") or "5432",
        'OPTIONS': {
            'sslmode': 'disable'
        },
        "TEST": {}
    },
}
DEBUG = True
