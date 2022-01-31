from django.urls import path

from .views import UserList, get_key

urlpatterns = [
    path('view-data-api/', UserList.as_view()),
    path('get-key/', get_key),
]
