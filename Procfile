web: newrelic-admin run-program gunicorn sparmed.wsgi:application -w $WEB_CONCURRENCY -k gevent --max-requests 500
worker: celery worker --app=tasks.app