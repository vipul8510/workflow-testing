if [ -z "$ENVIRONMENT" ]
then
    ENVIRONMENT='development'
fi
echo "environment is ------------------ ${ENVIRONMENT}"
export SIMPLE_SETTINGS=settings.${ENVIRONMENT}

echo "Run database migrations"
python3 manage.py makemigrations

echo "Apply database migrations"
python3 manage.py migrate

echo "Starting server"
gunicorn testing.wsgi:application --bind 0.0.0.0:8000