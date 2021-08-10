from django.db import models


class SomeModel(models.Model):
    some_field_str = models.CharField(max_length=255)
    some_field_int = models.PositiveIntegerField()
    some_field_boolean = models.BooleanField(default=False)