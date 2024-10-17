from .base import *

#es el modo de depuracion, nos muestra el error detallado
DEBUG = True 

# huespedes permitidos, quien puede acceder a la app
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] 
# engine = sistema de bases
DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.sqlite3",
        "NAME" : BASE_DIR / "db.sqlite",
    }
}
#establece una variable  de entorno de desarrollo
os.environ["DJANGO_PORT"] = "3000"