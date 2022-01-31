import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_import.settings')

app = Celery('service_import')
app.config_from_object('django.conf:settings', namespace='CELERY')

task_routes = {
    'get_data.tasks.recive_api_task': {'queue': 'queue_service_import'},
    }
app.conf.task_routes = task_routes
app.autodiscover_tasks()
