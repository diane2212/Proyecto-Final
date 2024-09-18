from .base import *

DEBUG = False #para que no muestre detalles del error

# TODO: Dejar solo el dominio de produccion
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] 

# TODO: Cambiar la configuracion de la base de datos para produccion
DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.sqlite3",
        "NAME" : BASE_DIR / "db.sqlite",

        #En caso de usar postgresql
        #"ENGINE": "django.db.backends.postgresql",

        #en caso de usar mysql
        #"ENGINE": "django.db.backends.mysql",

        # "name" : os.getenv("DB_NAME"), valor de la variable de entorno BD_name en 
        # "user" : os.getenv ("DB_USER")
        # "password" : os.getenv("DB_PASSWORD")
        #"host" : os.getenv("DB_HOST")
        #"port" : os.getenv("DB_PORT")
    }
}

os.environ["DJANGO_PORT"] = "8080"