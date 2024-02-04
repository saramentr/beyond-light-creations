from django.db import models
import uuid

# Create your models here.
class Todo(models.Model):
    result = models.JSONField()
    result_id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )

    status = models.CharField(max_length=50)
    timeout = models.PositiveIntegerField(null=True)
  
    type = models.TextField(
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'Todos'
