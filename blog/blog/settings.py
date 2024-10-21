import os  #para cceder a las variables de entorno
from dotenv import load_dotenv
#do= punto, env = (.env)

load_dotenv() #leera todas las variables en .env
#definir la v de entorno, si no esta definida por defecto sera development
DJANGO_ENV = os.getenv("DJANGO_ENV", "development")

if DJANGO_ENV == "production":
    from.configurations.production import *
else:
    from.configurations.local import *
