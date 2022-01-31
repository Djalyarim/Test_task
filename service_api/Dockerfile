FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY /service_api/. . 
RUN pip3 install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000 --insecure