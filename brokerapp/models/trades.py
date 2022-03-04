from django.db.models import (
    Model,
    CharField,
    DateField,
    PositiveIntegerField,
    PositiveBigIntegerField,
    BooleanField,
    ForeignKey,
    CASCADE,
)

from brokerapp.models import Broker


class Trade(Model):
    TRADE_TYPES = (
        ('buy', 'Buy'),
        ('sale', 'Sale'),
    )

    date = DateField()
    title = CharField(
        max_length=150,
    )
    price = PositiveIntegerField(
        help_text='в центах',
    )
    buy_or_sale = CharField(
        max_length=5,
        choices=TRADE_TYPES,
    )
    has_tax = BooleanField(
        default=True,
    )
    quantity = PositiveIntegerField(
        default=10,
    )
    amount = PositiveBigIntegerField(
        editable=False,
        null=True,
    )
    broker = ForeignKey(
        Broker,
        on_delete=CASCADE,
    )

    def __str__(self):
        return f"{self.title} — {self.broker}"
