#!/bin/sh

# Celery Worker Main
celery -A app.main.celery_app worker -Q test_queue -c 1 -l INFO -n test &

# Celery Scheduler
celery -A app.main.celery_app beat -l INFO -s /tmp/celerybeat-schedule &
