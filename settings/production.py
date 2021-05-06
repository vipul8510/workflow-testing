import os
import json

from dotenv import load_dotenv

load_dotenv(".env.production")

SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

DEBUG = os.getenv('DEBUG')
print ('DEBUG is ', DEBUG)
try:
    DEBUG = json.loads(DEBUG)
except ValueError:
    DEBUG = True

POSTGRESQL = {
    "db_name": os.getenv('POSTGRES_DB'),
    "user": os.getenv('POSTGRES_USER'),
    "password": os.getenv('POSTGRES_PWD'),
    "host": os.getenv('POSTGRES_HOST'),
    "port": os.getenv('POSTGRES_PORT'),
}
