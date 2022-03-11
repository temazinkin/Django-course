from django.shortcuts import render

from brokerapp.models import Trade


def index(request):
    trades = Trade.objects.all()
    title = 'Страница с транзакциями'
    context = {
        'title': title,
        'page_title': title,
        'trades': trades,
    }
    return render(request, 'brokerapp/index.html', context=context)


def page(request):
    title = 'О компании'
    context = {
        'title': title,
        'page_title': title,
    }
    return render(request, 'brokerapp/about.html', context=context)
