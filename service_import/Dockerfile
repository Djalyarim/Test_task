FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY /service_import/. . 

COPY ./compose/local/django/celery/worker/service_import/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/flower/service_import/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

RUN pip3 install -r requirements.txt
CMD python ./service_import/manage.py runserver 0.0.0.0:8001