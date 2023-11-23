from django.db import models


class Item(models.Model):
    """Модель предмета."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
