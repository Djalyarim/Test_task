[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)


# Тестовое задание


Убедитесь что у вас установлен Docker, если нет - установите:
```
https://www.docker.com/products/personal
```

## Подготовка и запуск проекта
### Склонируйте репозиторий на локальную машину:
```
git clone https://github.com/Djalyarim/Test_task.git
```
### Локально переименуйте файлы .env.template в директориях service_api, service_import, service_data в .env

### В первом теримнале из корневой директории запустите команду на сбор и запуск контейнеров:
```
docker-compose build && docker-compose up -d && docker-compose logs -f
```
### Подождите запуска всех контейнеров

### Во втором терминале несколько раз запустите команду:
```
curl -X GET http://127.0.0.1:8001/run-import-task/ 
```
### Если сервис service_api сгенерировал вес с нечетной целой частью, то вес сохраняется в postgres




