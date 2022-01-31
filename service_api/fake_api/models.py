from django.db import models


class UserWeight(models.Model):
    day = models.DateTimeField('Дата публикации')
    user_id = models.IntegerField()
    weight = models.FloatField()
    unit = models.CharField(max_length=20)
