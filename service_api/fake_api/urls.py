from django.urls import path

from .views import fake_api

urlpatterns = [
    path('external-fake-api/', fake_api),
]
