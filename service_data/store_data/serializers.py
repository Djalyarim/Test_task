from rest_framework import serializers

from .models import UserWeight


class UserWeightSerializer(serializers.ModelSerializer):
    day = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])

    class Meta:
        fields = ('day', 'user_id', 'weight')
        model = UserWeight
