FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.lock .
RUN pip install --no-cache-dir -r requirements.lock
COPY . .
RUN python manage.py collectstatic --noinput && useradd --create-home lab && mkdir /data && chown lab:lab /data
USER lab
EXPOSE 8000
CMD ["gunicorn", "gitlab_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--access-logfile", "-"]
