from datetime import date, datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from crawlers.textcrawler import textcrawler


def soloshow(links, name_list, site_page_cnt):
    print('soloshow')

    now = datetime.now()
    req = Request("http://soloshow.online/version01.html", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    web_byte = urlopen(req).read()
    rawhtml = web_byte.decode('utf-8')
    soup = BeautifulSoup(rawhtml, features="html.parser")

    # dd/mm/YY
    for a in soup.find_all('div', {"class": "col-sm-6 col-md-3"}):
        for b in a.find_all('a', href=True):
            if "html" in b['href'] or "htnl" in b['href']:
                url = "http://soloshow.online/" + b['href']
            elif '/' not in b['href'] and '.' not in b['href']:
                url = "http://soloshow.online/" + b['href']
            else:
                url = b['href']
            if url not in links:
                d1 = now.strftime("%d/%m %H:%M:%S")
                links[url] = [b.text, d1]
                print("http://soloshow.online/ ", b.text, url)
            print('printing' + url)
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
            web_byte = urlopen(req).read()
            subRawHtml = web_byte.decode('utf-8')
            textcrawler(url, name_list, site_page_cnt, subRawHtml)

