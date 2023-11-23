from django.contrib import admin
from item.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Админ-панель модели предмета."""

    fields = ('name', 'description', 'price')
    list_display = ('id', 'name', 'description', 'price')
