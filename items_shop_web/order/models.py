from django.db import models
from item.models import Item


class Order(models.Model):
    """Модель заказа."""

    items = models.ManyToManyField(Item)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True)


class Discount(models.Model):
    """Модель скидки."""

    name = models.CharField(max_length=100)
    discount_percent = models.FloatField()

    def __str__(self):
        return self.name


class Tax(models.Model):
    """Модель налога."""

    name = models.CharField(max_length=100)
    tax_percent = models.FloatField()

    def __str__(self):
        return self.name
