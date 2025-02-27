from django.db import models
import uuid
# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name