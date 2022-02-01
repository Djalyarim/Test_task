from cgitb import lookup

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import UserWeight
from .serializers import UserWeightSerializer
from .tasks import get_key_task


class UserList(generics.ListAPIView):
    queryset = UserWeight.objects.all()
    serializer_class = UserWeightSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['user_id', ]
    ordering_fields = ['day', ]
    ordering = ['day', ]


@api_view(['POST'])
def get_key(request):
    get_key_task.delay(request.data)
    return HttpResponse('')
