#! /usr/bin/env sh
set -e

# Start Gunicorn
echo "Starting $APP_MODULE with $WORKER_CLASS"
exec gunicorn -k "uvicorn.workers.UvicornWorker" -c "./gunicorn_conf.py" --chdir "./api" "main:app"