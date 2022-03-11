from django.urls import path

from brokerapp.views import index, page

urlpatterns = [
    path('', index),
    path('about/', page),
]
