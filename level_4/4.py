#!/usr/bin/python3
import requests
from random import randint
from proxies import proxies as new_proxies


def vote_4_pedro():
    URL = 'http://158.69.76.135/level4.php'
    payload = {
        'id': 332,
        'holdthedoor':'Submit',
        'key':'0'
    }
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Referer':URL
    }
    cookie = {
        'HoldTheDoor': '0',
        'Expires':'0',
        'Max-Age':'0'
    }
    
    votes = 0
    i = 1
    while votes < len(new_proxies):
        new_proxy = new_proxies[i]
        proxies = {'http': new_proxy}
        i += 1
        print(proxies)
        try:
            r = requests.post(URL, data=payload, headers=header, cookies=cookie, proxies=proxies)
        except:
            print(r.status_code)
        print("Voted: {} times".format(votes)) 
        votes += 1

vote_4_pedro()
