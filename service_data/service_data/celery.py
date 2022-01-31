import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_data.settings')

app = Celery('service_data')
app.config_from_object('django.conf:settings', namespace='CELERY')

task_routes = {
    'store_data.tasks.get_key_task': {'queue': 'queue_service_data'},
    }
app.conf.task_routes = task_routes
app.autodiscover_tasks()
