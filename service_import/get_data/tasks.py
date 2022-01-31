import redis
import requests
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task()
def recive_api_task():
    conn = redis.StrictRedis(
        host='redis',
        charset='utf-8',
        decode_responses=True
    )
    try:
        response = requests.get('http://my-service-api:8000/external-fake-api/').json()
    except Exception as e:
        logger.error('No signal', e)
    conn.hmset('my_dict', response)
    data = {'take_key': 'my_dict'}
    try:
        requests.post('http://my-service-api-data:8002/get-key/', data=data)
        return data
    except Exception as e:
        logger.error('No signal', e)
