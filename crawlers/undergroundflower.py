from datetime import date, datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def undergroundflower(links):
    print('undergroundflower')

    now = datetime.now()
    req = Request('http://undergroundflower.com/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    web_byte = urlopen(req).read()
    rawhtml = web_byte.decode('utf-8')
    soup = BeautifulSoup(rawhtml, features="html.parser")
    # dd/mm/YY
    for a in soup.find_all('a', href=True):
        if a.text != "About" and not a['href'] in links:
            d1 = now.strftime("%d/%m %H:%M:%S")
            links[a['href']] = [a.text, d1]
            print("http://undergroundflower.com/ ", a.text, a['href'])
        else:
            print("already found")

