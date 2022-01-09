from django.urls import re_path
from .consumers import WSConsumer

ws_urlpatterns = [
    re_path('ws/cities', WSConsumer.as_asgi())
]