web: newrelic-admin run-program python ./manage.py gunicorn sparmed.wsgi:application -w 3 -k gevent --max-requests 500