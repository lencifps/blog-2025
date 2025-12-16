import os
from dotenv import load_dotenv

load_dotenv()

DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECRET_KEY = '1234'

if DJANGO_ENV == 'production':
    from.configurations.production import *
else:
    from.configurations.local import *