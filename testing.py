import caching
import json 
# api url = 'https://api.exchangeratesapi.io/latest'

def main():
    
    if caching.read_cache()[0]:
        response = caching.read_cache()[1]
    else:
        response = caching.make_cache()
    print(response)
       
if __name__ == '__main__':
    main()
