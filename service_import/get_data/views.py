from django.http import HttpResponse
from rest_framework.decorators import api_view

from .custom_log import log
from .tasks import recive_api_task


@api_view(['GET'])
def recive_api(request):
    log.info('---------------- Начало запроса ---------------')
    recive_api_task.delay()
    return HttpResponse('')
