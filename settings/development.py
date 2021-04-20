import os
import json

from dotenv import load_dotenv


print ('came inside DEVELOPMENT mode')
load_dotenv(".env.development")

SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

DEBUG = os.getenv('DEBUG')
try:
    DEBUG = json.loads(DEBUG)
except ValueError:
    DEBUG = True
print ('DEBUG is ', DEBUG)

POSTGRESQL = {
    "db_name": os.getenv('POSTGRES_DB'),
    "user": os.getenv('POSTGRES_USER'),
    "password": os.getenv('POSTGRES_PWD'),
    "host": os.getenv('POSTGRES_HOST'),
    "port": os.getenv('POSTGRES_PORT'),
}