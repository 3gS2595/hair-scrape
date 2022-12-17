from datetime import date, datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def soloshow(links):
    print('soloshow')

    now = datetime.now()
    req = Request("http://www.soloshow.online/", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    web_byte = urlopen(req).read()
    rawhtml = web_byte.decode('utf-8')
    soup = BeautifulSoup(rawhtml, features="html.parser")

    # dd/mm/YY
    for a in soup.find_all('div', {"class": "col-sm-6 col-md-3"}):
        flag = 0
        html = "";
        d1 = now.strftime("%d/%m %H:%M:%S")
        for b in a.find_all('a', href=True):
            if not ("http://soloshow.online/" + b['href']) in links and "html" in b['href']:
                html = "http://soloshow.online/" + b['href']
                flag = 1
            else:
                flag = 0
            if flag == 1:
                for c in a.find_all('i'):
                    d1 = now.strftime("%d/%m %H:%M:%S")
                    links[html] = [c.text, d1]
                    print("http://soloshow.online/ ", c.text, html)
