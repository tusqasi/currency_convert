from datetime import date
from os import path
import requests
import json

def get_rate():
    if read_cache()[0]:
        response = read_cache()[1]
    else:
        response = make_cache()
    return response

def make_cache(base='USD', cache_name='cache.json'):
    # now = date.today()
    # now.strftime("%m-%d-%y")
    response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}').json() 
    with open(cache_name, 'w') as f:
        json.dump(response, f)

def read_cache(cache_name='cache.json'):
    now = date.today() 
    if path.exists(f"./{cache_name}"):
        with open(cache_name,'r') as f:
            cached_response = json.load(f)
            cached_date = date(*[int(x) for x in cached_response['date'].split('-',2)])
            if (now - cached_date).days > 2:
                return [0]
            else:
                return [1, cached_response]
