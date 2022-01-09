from channels.generic.websocket import WebsocketConsumer
import redis
import json
import time

from .views import get_weather, get_cities

redis_client = redis.StrictRedis(host='redis',port=6379, db=0, charset="utf-8", decode_responses=True)


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:         
            get_cities(redis_client)
            self.send(json.dumps(get_weather(redis_client)))
            time.sleep(5)           
            
       


