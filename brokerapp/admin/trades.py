from brokerapp.models import Trade
from django.contrib.admin import (
    ModelAdmin,
    register,
)


@register(Trade)
class TradeAdmin(ModelAdmin):
    save_as = True
    list_display = (
        '__str__',
        'date',
        'title',
        'price',
        'buy_or_sale',
        'has_tax',
        'quantity',
        'amount',
        'broker',
    )
    list_display_links = (
        '__str__',
        'title',
    )
    list_editable = (
        'date',
        'has_tax',
        'buy_or_sale',
        'has_tax',
        'quantity',
        'broker',
    )
    list_filter = (
        'has_tax',
        'broker',
    )
