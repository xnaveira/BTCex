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

def main():
    exchange_url = 'https://www.fybse.se/'
    #exchange_url = 'https://api.bitcoinaverage.com/'
    #ticker_part = 'ticker/global/'
    ticker_part = 'api/'
    currency_part = 'SEK/ticker.json'

    curl_address = exchange_url + ticker_part + currency_part
    old_ask = 0
    old_bid = 0

    while (1):
        curl_call = 'curl -H "Accept:application/json" -X GET -k  ' + curl_address + ' 2>/dev/null'
        response=subprocess.check_output(curl_call, shell=True)
        response_json = json.loads(response)
        new_ask = response_json["ask"]
        new_bid = response_json["bid"]
        if new_ask > old_ask:
            ask_color = 'green'
        elif new_ask > old_ask:
            ask_color = 'red'
        else:
            ask_color = 'cyan'
        if new_bid > old_bid:
            bid_color = 'green'
        elif new_bid < old_bid:
            bid_color = 'red'
        else:
            bid_color = 'cyan'
        print_ask = ask_color + '(new_ask)'
        print_bid = bid_color + '(new_bid)'
        print 'Ask: {0} | Bid: {1}'.format(eval(print_ask),eval(print_bid))
        old_ask = new_ask
        old_bid = new_bid
        time.sleep(10)

if __name__ == "__main__":
    main()


