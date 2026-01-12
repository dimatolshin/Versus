import os
import django
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
app = Celery('app')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update( task_acks_late=True, task_reject_on_worker_lost=True)
app.conf.broker_connection_retry_on_startup = True
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')