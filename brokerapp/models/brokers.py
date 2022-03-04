from django.db.models import (
    Model,
    CharField,
)


class Broker(Model):
    bank = CharField(
        max_length=30,
    )

    def __str__(self):
        return self.bank

    class Meta:
        db_table = 'brokers'
