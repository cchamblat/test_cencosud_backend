from django.shortcuts import render
from django.http import HttpResponse
import requests
import random
from datetime  import datetime



# Create your views here.

cities = ['Santiago','Zurich','Auckland','Sydney','London','Georgia']

def index(request):

    return HttpResponse('Hello, world')


def get_cities(redis_client):    
    for city in cities:
        success = False
        while success == False:
            if (random.random() < 0.1):
                success = False
                # print('How unfortunate! The API Request Failed')
                now = datetime.now()
                current_time = now.strftime('%H:%M:%S')
                redis_client.hset('api.errors', current_time, 'How unfortunate! The API Request Failed')
                # print(redis_client.hget('api.errors', current_time))

            else:
                success = True
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=621e9be55a4700821eb00b92c87ad677'         
                r = requests.get(url.format(city)).json()
                redis_client.hset('cities', city, str(r['coord']['lat']) + '_' + str(r['coord']['lon']))
                # print(redis_client.hget('cities', city))
                # print(city)


               
    # get_weather(redis_client)
    return None   

    
def get_weather(redis_client):
    response = {}        
    for city in cities:
        success = False
        while success == False:
            if (random.random() < 0.1):
                success = False
                now = datetime.now()
                current_time = now.strftime('%H:%M:%S')
                redis_client.hset('api.errors', current_time, 'How unfortunate! The API Request Failed' )                
            else:
                success = True
                coords = str(redis_client.hget('cities', city))                
                base_time =  datetime.timestamp(datetime.utcnow())
                url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=621e9be55a4700821eb00b92c87ad677'
                lat, lon = coords.split('_')
                r = requests.get(url.format(lat, lon)).json()
                response [city] = {                
                'temp': int(r['main']['temp'] - 273),                       
                'local_time': str(datetime.fromtimestamp(base_time + r['timezone']).strftime('%H:%M:%S %p'))                                                    
                }
    
    print(response)
                
    # print(redis_client.hgetall('api.errors'))      

    return response
        




























    



