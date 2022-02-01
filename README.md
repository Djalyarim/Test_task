[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)


# Проект - сбор и обработка данных 

Тестовое задание состоит из 8-ми контейнеров:
service_api         - отдельное приложение
service_import      - отдельное приложение
service_data        - отдельное приложение
celery_worker       - worker для service_import
celery_worker_2     - worker для service_data
flower              - мониторинг
postgres            - БД 
redis               - БД

## Подготовка и запуск проекта

Убедитесь что у вас установлен Docker, если нет - установите:
```
https://www.docker.com/products/personal
```

### Склонируйте репозиторий на локальную машину:
```
git clone https://github.com/Djalyarim/Test_task.git
```
### Для удобства тестирования все файлы .env присутствуют в проекте

### В первом теримнале из корневой директории проекта запустите команду на сбор и запуск контейнеров:
```
docker-compose build && docker-compose up -d && docker-compose logs -f
```
### Подождите запуска всех контейнеров

### Во втором терминале несколько раз запустите команду:
```
curl -X GET http://127.0.0.1:8001/run-import-task/
```
Каждый запуск берет значение из сервиса service_api.
Если сервис service_api сгенерировал вес с нечетной целой частью, то вес сохраняется в postgres.
Для удобства проверки service_api генерирует пользователей с id от 1 до 10.

### Flower - мониторинг задач Celery
```
http://127.0.0.1:5557/tasks
```

### Service_api - имитация API
```
http://127.0.0.1:8000/external-fake-api/
```

### Service_data - просмотр данных из postgres с фильтром по user_id и сортировкой по дню
```
http://127.0.0.1:8002/view-data-api/?user_id=
```




