from decimal import Decimal

from django.db.models import (
    Model,
    CharField,
    DateField,
    PositiveIntegerField,
    BooleanField,
    ForeignKey,
    CASCADE,
    DecimalField,
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
    price = DecimalField(
        max_digits=14,
        decimal_places=4,
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
    amount = DecimalField(
        max_digits=14,
        decimal_places=4,
        editable=False,
        null=True,
    )
    broker = ForeignKey(
        Broker,
        on_delete=CASCADE,
    )

    def __str__(self):
        return f"{self.title} — {self.broker}"

    def save(self, *args, **kwargs):
        price = self.price
        quantity = self.quantity
        amount = price * quantity
        if self.has_tax:
            amount = amount * Decimal(0.9)
        self.amount = amount
        super(Trade, self).save(args, kwargs)
