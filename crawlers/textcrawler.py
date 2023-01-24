from datetime import date, datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import nltk
from nameparser.parser import HumanName


def textcrawler(key, name_list, site_page_cnt, rawhtml):
    tokens = nltk.tokenize.word_tokenize(rawhtml)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary=False)
    person = []
    name = ""
    site = key.split('//')[1].split('/')[0]
    if site not in site_page_cnt:
        site_page_cnt[site] = 1
    else:
        site_page_cnt[site] = site_page_cnt[site] + 1
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1:  # avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in name_list:
                name_list[name[:-1]] = [1, key]
                print(name[:-1])
            else:
                name_list[name[:-1]][0] = name_list[name[:-1]][0] + 1
                name_list[name[:-1]].append(key)
            name = ''
        person = []
