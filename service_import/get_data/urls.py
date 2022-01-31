from django.urls import path

from .views import recive_api

urlpatterns = [
    path('run-import-task/', recive_api),
]
