from datetime import datetime
from random import randint, uniform

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserWeightSerializer


@api_view(['GET'])
def fake_api(request):
    date_now = datetime.now().strftime('%Y-%m-%d')
    generate_fake_api = {
        'day': date_now,
        'user_id': randint(1, 10),
        'weight': round(uniform(80, 120), 1),
        'unit': 'kg'
    }
    serializer = UserWeightSerializer(data=generate_fake_api)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
