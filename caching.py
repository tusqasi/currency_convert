from os import path
import time
import requests
import json

def offline():
    try:
        requests.get("https://duckduckgo.com")        
    except requests.ConnectionError:
        print("offline")
        return 1
    return 0

def get_rate():
    if read_cache()[0]:
        response = read_cache()[1]
    else:
        make_cache()
        get_rate()
    return response

def make_cache(base='', cache_name='cache.json'):
    # now = date.today()
    # now.strftime("%m-%d-%y")
    
    response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}')
    
    if respone.status_code != 200:
        raise ApiError(f'Some Error')
     
    response = response.json() 

    response['time'] = time.time()
    with open(cache_name, 'w') as f:
        json.dump(response, f)

def read_cache(cache_name='cache.json'):
    now = time.time()
    if path.exists(f"./{cache_name}"):
        with open(cache_name,'r') as f:
            cached_response = json.load(f)
            cached_time = cached_response['time']
            if offline():
                return [1, cached_response]        
            elif now - cached_time > 3600:
                return [0]
            else:
                return [1, cached_response]
    else:
        make_cache()
        read_cache()
