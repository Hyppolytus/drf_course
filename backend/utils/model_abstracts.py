import uuid
from django.db import models


class Model(models.Model):
    # This is essentially a custom model field, it will be used to generate a unique id for each model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True