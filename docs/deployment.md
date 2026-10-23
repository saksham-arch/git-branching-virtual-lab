# Deployment exercise

The Django service and FastAPI service are independent. Django accounts do not authenticate FastAPI requests. Keep the unauthenticated teaching API bound to `127.0.0.1`; add authentication before exposing it to a network.

## Reproducible local setup

Use Python 3.13 and install requirements.lock. Run migrations before starting either Django or Gunicorn. The custom user model is present in the first course migration. The course uses a new `course.sqlite3` so an older `db.sqlite3` remains untouched; do not switch AUTH_USER_MODEL in a database that already contains Django auth tables.

## Django container

```bash
docker build -t django-vlab .
# Create a volume for persistent course data.
docker volume create django-vlab-data
# Replace the secret value and hostname. Terminate HTTPS at your reverse proxy.
docker run --rm -v django-vlab-data:/data \
  -e DJANGO_DB_PATH=/data/course.sqlite3 \
  django-vlab python manage.py migrate

docker run --rm -p 127.0.0.1:8000:8000 -v django-vlab-data:/data \
  -e DJANGO_DB_PATH=/data/course.sqlite3 \
  -e DJANGO_DEBUG=0 -e DJANGO_SECRET_KEY='replace-with-a-long-random-secret' \
  -e DJANGO_ALLOWED_HOSTS='lab.example.edu' \
  django-vlab
```

The image uses Gunicorn, not runserver. Its `/app/staticfiles/` must be served at `/static/` by the reverse proxy or an asset service. `collectstatic` runs at image build. Mount or copy those assets into the static server. Configure a TLS proxy to forward requests, preserve Host, and redirect HTTP to HTTPS. Secure cookies and SSL redirects are enabled when DEBUG=0. If the proxy terminates TLS, configure `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')` only behind a trusted proxy that strips client-supplied forwarding headers; otherwise use end-to-end TLS. The default settings intentionally do not trust that header.

Configure a Django SMTP backend and EMAIL_HOST/PORT/credentials through deployment-specific settings before relying on email delivery. The shipped backend is console output for local teaching. Keep secrets outside Git. Back up the database volume; use PostgreSQL for concurrent classroom production use. Configure host-level request limits for authentication endpoints.

## Local service checks

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
python -m pytest api/tests.py -q
python manage.py collectstatic --noinput
# Supply production environment variables, then inspect remaining warnings:
python manage.py check --deploy
```

For the FastAPI practical: `uvicorn api.main:app --host 127.0.0.1 --port 8001`. Set FASTAPI_DB_PATH to a persistent writable location. Synchronous SQLite endpoints run in FastAPI's worker thread pool; the health endpoint illustrates an async handler. Swagger UI uses externally hosted documentation assets by default and requires network access; `/openapi.json` is local.

## Release verification

Check the real HTTPS URL, static assets, login/logout, CSRF failure, password reset email delivery, permission-denied response, CSV/PDF downloads, persistent data after restart, backups and application logs. Record the host and commit SHA. Container source and local tests alone are not evidence of an actual hosted deployment.
