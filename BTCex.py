#!/usr/bin/python
"""
March 2014
Xavier Naveira
xnaveira@gmail.com
"""
import sys
import subprocess
import json
import urllib
import time
from fabric.colors import red,green,yellow,white,cyan

def get_color(new,old):
    if new>old:
        return 'green'
    elif new<old:
        return 'red'
    else:
        return 'cyan'


def main():
    exchange_url = 'https://www.fybse.se/'
    ticker_part = 'api/'
    currency_part = 'SEK/ticker.json'

    curl_address = exchange_url + ticker_part + currency_part
    old = (0,0)

    while (1):
        curl_call = 'curl -H "Accept:application/json" -X GET -k  ' + curl_address + ' 2>/dev/null'
        response=subprocess.check_output(curl_call, shell=True)
        response_json = json.loads(response)
        new = (response_json["ask"],response_json["bid"])
        color = (get_color(new[0],old[0]),get_color(new[1],old[1]))
        printo = (color[0] + '(new[0])',color[1] + '(new[1])')
        print 'Ask: {0} | Bid: {1}'.format(eval(printo[0]),eval(printo[1]))
        old = new
        time.sleep(60)

if __name__ == "__main__":
    main()


