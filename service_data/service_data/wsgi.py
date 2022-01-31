import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_data.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

application = get_wsgi_application()
