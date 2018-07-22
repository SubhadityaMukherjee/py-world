import time

import requests
import urllib
from bs4 import BeautifulSoup
from lxml import html
from urllib.request import Request
from bs4 import Comment
import os


def search(keywords, max_results=None):
    url = 'https://duckduckgo.com/html/'
    params = {
        'q': keywords,
        's': '0',
    }

    yielded = 0
    while True:
        res = requests.post(url, data=params)
        doc = html.fromstring(res.text)

        results = [a.get('href') for a in doc.cssselect('#links .links_main a')]
        for result in results:
            yield result
            time.sleep(0.1)
            yielded += 1
            if max_results and yielded >= max_results:
                return
        try:
            form = doc.cssselect('.results_links_more form')[-1]
        except IndexError:
            return
        params = dict(form.fields)


def list_of_links():
    l = []
    for link in search(input('Enter your search term: '),
                       max_results=int(input('Enter number of websites to search from: '))):
        l.append(link)
    c = int(input("Enter 1 if you want to search wiki and 2 if you don't: "))
    if c == 2:
        le = len(l)
        for a in range(le):
            if "wiki" in l[a]:
                l.pop(a)
                le-=1
    return l


def clean(soup):
    [x.extract() for x in soup.find_all('script')]
    [x.extract() for x in soup.find_all('style')]
    [x.extract() for x in soup.find_all('meta')]
    [x.extract() for x in soup.find_all('noscript')]
    [x.extract() for x in soup.find_all(text=lambda text: isinstance(text, Comment))]
    [x.extract() for x in soup.find_all('head')]
    [x.extract() for x in soup.find_all("header")]
    [x.extract() for x in soup.find_all("banner")]
    return soup


def clean_file():
    f = open("Data.txt", "r", encoding='utf-8', errors='ignore')
    na = input("Enter a name for your file: ")
    p = open(na + '.txt', "a+", encoding='utf-8', errors='ignore')
    l = f.readlines()
    for a in l:
        if len(a.split()) < 1:
            p.write(" ")
        elif len(a.split()) == 1:
            p.write(a + '-')
        else:
            p.write(a + '\n')
    p.close()


def scrape():
    c = 1
    f = open("Data.txt", "w+", encoding='utf-8', errors='ignore')
    l = list_of_links()
    t = ''
    for a in l:
        try:
            req = urllib.request.Request(a)
            new = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(new, "lxml")
            soup = clean(soup)
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            t += text + '\n'
            f.write(t)
            print('Done link:', c)
            c += 1
            time.sleep(0.1)
        except:
            print("There is a problem with this link. Trying another.\n")
            c += 1
            time.sleep(0.1)
            pass
    f.write(t)
    f.close()
    clean_file()


scrape()
