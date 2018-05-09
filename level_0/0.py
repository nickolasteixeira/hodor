#!/usr/bin/python3
import requests

payload = {
    'id': 332,
    'holdthedoor': 'Submit'
}
URL = 'http://158.69.76.135/level0.php'
votes = 0
while votes < 1024:
    r = requests.post(URL, data=payload)
    votes += 1

print("Number of Votes counted:{}".format(votes))
