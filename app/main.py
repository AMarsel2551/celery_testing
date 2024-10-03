import requests
from celery import Celery
from celery.schedules import crontab
from kombu import Queue


celery_app = Celery(
    'celery_testing',
    broker=f"redis://:Marc2551@37.230.113.58:6379",
    backend=f"redis://:Marc2551@37.230.113.58:6379",
    broker_connection_retry_on_startup=True,
)


# celery_app.conf.timezone = "Europe/Moscow"
# celery_app.conf.enable_utc = False


celery_app.conf.task_queues = (
    Queue(name='test_queue'),
)


celery_app.conf.beat_schedule = {
    'generate_out_report': {
        'task': 'test',
        'schedule': crontab(hour="16", minute="25"),
        # 'schedule': 2,
        'options': { 'queue': 'test_queue' },
    },
}


@celery_app.task(name="test", queue='test_queue', soft_time_limit=60 * 10)
def ctest():
    requests.post(
        f'https://api.telegram.org/bot7136248500:AAE-6nXdSvqiPaFLyJPeTmNjUf8M2L4opsg/sendMessage',
        data={ 'chat_id': 1112458996, 'text': 'TEST', 'parse_mode': 'HTML'},
    )