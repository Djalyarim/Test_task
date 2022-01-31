import uuid

from django.db import models


class UserWeight(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_id = models.IntegerField()
    day = models.DateField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'user_weight'
