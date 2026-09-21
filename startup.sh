#!/usr/bin/env bash
#
# Shared entrypoint for both Azure App Service (code deploy) and the local
# Docker image. Runs the one-time deploy steps, then serves the app.
#
set -euo pipefail

cd "$(dirname "$0")"

echo "==> Applying database migrations"
python manage.py migrate --noinput

echo "==> Collecting static files"
python manage.py collectstatic --noinput

if [ "$#" -gt 0 ]; then
    echo "==> Starting: $*"
    exec "$@"
fi

echo "==> Starting gunicorn on 0.0.0.0:${PORT:-8000}"
exec gunicorn savannah.wsgi:application \
    --bind "0.0.0.0:${PORT:-8000}" \
    --workers "${GUNICORN_WORKERS:-3}" \
    --timeout "${GUNICORN_TIMEOUT:-600}" \
    --access-logfile - \
    --error-logfile -
