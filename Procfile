web: newrelic-admin run-program gunicorn sparmed.wsgi:application -w $WEB_CONCURRENCY -k gevent --max-requests 500; python manage.py update_index; python manage.py clearsessions; python manage.py cleancarts;