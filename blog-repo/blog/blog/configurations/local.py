from .base import *

DEBUG = True 

# TODO: Dejar solo el dominio de produccion
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] 

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.sqlite3",
        "NAME" : BASE_DIR / "db.sqlite",
    }
}

os.environ["DJANGO_PORT"] = "3000"