from brokerapp.models import Broker
from django.contrib.admin import (
    ModelAdmin,
    register,
)


@register(Broker)
class BrokerAdmin(ModelAdmin):
    pass
