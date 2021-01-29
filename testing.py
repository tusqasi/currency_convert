from caching import *
import json 
import sys
# api url = 'https://api.exchangeratesapi.io/latest'
    
def main():
    amt = float(sys.argv [1])
    base_cur = sys.argv[2]
    target_cur = sys.argv[3]

    rates = get_rate()['rates']

    base_rate = rates[base_cur]
    target_rate = rates[target_cur]
    final = amt / base_rate * target_rate
    print(final)

if __name__ == '__main__':
    main()
