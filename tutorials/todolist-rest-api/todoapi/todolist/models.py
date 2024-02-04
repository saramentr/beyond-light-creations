from django.db import models
import uuid

# Create your models here.
class Todo(models.Model):
    result = models.CharField(max_length=50)
    result_id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )

    status = models.CharField(max_length=50)
    timeout = models.PositiveIntegerField(default=0)
  
    type = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )

  class Meta:
    db_table = 'Todos'
