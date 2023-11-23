from django.contrib import admin
from order.models import Discount, Order, Tax


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админ-панель модели заказа."""

    list_display = ('id',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    """Админ-панель налога."""

    fields = ('name', 'tax_percent')
    list_display = ('id', 'name', 'tax_percent')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """Админ-панель скидки."""

    fields = ('name', 'discount_percent')
    list_display = ('id', 'name', 'discount_percent')
