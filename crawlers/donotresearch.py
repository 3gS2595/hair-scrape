from datetime import date, datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def donotresearch(links):
    print('donotresearch')
    now = datetime.now()
    req = Request('https://finalhotdesert.com/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    web_byte = urlopen(req).read()
    rawhtml = web_byte.decode('utf-8')
    soup = BeautifulSoup(rawhtml, features="html.parser")
    for a in soup.find_all('div', {"class": "post-preview"}):
        for b in a.find_all('a', href=True):
            if b.text != "About" and not b['href'] in links and 'post' in b['href']:
                d1 = now.strftime("%d/%m %H:%M:%S")
                links["https://donotresearch.net/" + b['href']] = [b.text, d1]
                print("https://donotresearch.net/", b.text, ("https://donotresearch.net/" + b['href']))
            else:
                print("already found")


