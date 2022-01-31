import redis
from celery import shared_task
from celery.utils.log import get_task_logger

from .serializers import UserWeightSerializer

logger = get_task_logger(__name__)


@shared_task()
def get_key_task(request):
    conn = redis.StrictRedis(
        host='redis',
        charset='utf-8',
        decode_responses=True
    )
    recive = conn.hgetall(request['take_key'])
    data = {
        'user_id': int(recive['user_id']),
        'day': recive['day'],
        'weight': recive['weight']}
    serializer = UserWeightSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    if int(recive['weight'][:-2]) % 2 == 0:
        return data
    serializer.save()
    return data
